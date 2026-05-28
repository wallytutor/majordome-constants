# -*- coding: utf-8 -*-
""" Build, import, and test the Python extension. """

import importlib
import sys
import shutil

from argparse import ArgumentParser
from argparse import BooleanOptionalAction
from pathlib import Path
from subprocess import run
from types import ModuleType


def build_and_import(name: str) -> ModuleType:
    """ Build and import the extension. """
    print("=" * 70)

    #region: argument parser
    parser = ArgumentParser("Build and import the extension.")

    parser.add_argument(
        "--release",
        action="store_true",
        help="build the extension in release mode."
    )
    parser.add_argument(
        "--build",
        action=BooleanOptionalAction,
        default=True,
        help="build the extension."
    )
    parser.add_argument(
        "--docs",
        action=BooleanOptionalAction,
        default=True,
        help="build the extension documentation."
    )
    parser.add_argument(
        "--open-docs",
        action="store_true",
        help="open the extension documentation after building."
    )
    args = parser.parse_args()
    #endregion: argument parser

    #region: parse arguments
    should_release = args.release
    should_build = args.build
    should_docs = args.docs

    mode = "release" if should_release else "debug"

    root_dir = Path(__file__).parent
    dll_path = root_dir / "target" / mode / f"{name}.dll"

    if not should_build and not dll_path.exists():
        print("No build required, but DLL not found. Building anyway...")
        should_build = True
    #endregion: parse arguments

    #region: clippy
    proc = run("cargo clippy --no-deps".split(), cwd=root_dir, check=True)

    if proc.returncode != 0:
        print(f"Error: Crate clippy failed with return code {proc.returncode}")
        sys.exit(1)
    #endregion: clippy

    #region: build
    if should_build:
        mode_name = "--release" if should_release else ""
        cmd = f"cargo build {mode_name}"
        proc = run(cmd.split(), cwd=root_dir, check=True)

        if proc.returncode != 0:
            print(f"Error: Crate build failed with code {proc.returncode}")
            sys.exit(1)
    #endregion: build

    #region: docs
    if should_docs:
        cmd = "cargo doc --no-deps"

        if args.open_docs:
            cmd += " --open"

        proc = run(cmd.split(), cwd=root_dir, check=True)

        if proc.returncode != 0:
            print(f"Error: Crate docs failed with code {proc.returncode}")
            sys.exit(1)
    #endregion: docs

    #region: copy
    if not dll_path.exists():
        print(f"Error: Compiled library not found at {dll_path}")
        sys.exit(1)

    pyd_path = dll_path.parent / f"{name}.pyd"
    sys.path.insert(0, str(dll_path.parent))

    if not shutil.copy2(dll_path, pyd_path):
        print(f"Error: Failed to copy {dll_path.name} to {pyd_path.name}")
        sys.exit(1)

    print(f"    Successfully copied {dll_path.name} to {pyd_path.name}")
    #endregion: copy

    #region: import
    try:
        extension = importlib.import_module(name)

        print("=" * 70)
        print(f"    Success! Extension {name} imported successfully.")
        print("")
        print("    Available contents:")

        for x in sorted(dir(extension)):
            if x.startswith("_"):
                continue
            print(f"    - {x}")

    except ImportError as e:
        print(f"Failed to import extension: {e}")
        sys.exit(1)
    #endregion: import

    print("=" * 70)
    return extension


if __name__ == "__main__":
    ext = build_and_import("majordome_constants")
