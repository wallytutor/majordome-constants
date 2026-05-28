#![deny(clippy::unwrap_used)]
#![deny(clippy::expect_used)]
#![deny(clippy::panic)]
#![deny(unused_must_use)]
#![deny(warnings)]

use pyo3::prelude::*;

mod elements;
pub mod prelude;

#[pymodule(name = "majordome_constants")]
pub mod majordome_constants {
    /// Mathematical constant π (pi).
    #[pymodule_export]
    pub const PI: f64 = std::f64::consts::PI;

    /// Avogadro's number (1/mol).
    #[pymodule_export]
    pub const AVOGADRO: f64 = 6.022_140_76e23;

    /// Boltzmann constant (J/K).
    #[pymodule_export]
    pub const BOLTZMANN: f64 = 1.380_649e-23;

    /// Elementary charge (C).
    #[pymodule_export]
    pub const ELECTRON_CHARGE: f64 = 1.602_176_634e-19;

    /// Faraday constant (C/mol).
    #[pymodule_export]
    pub const FARADAY: f64 = 96_485.332_12;

    /// Universal gas constant (J/(mol·K)).
    #[pymodule_export]
    pub const GAS_CONSTANT: f64 = 8.314_462_618_153_24;

    /// Conventional gravitational acceleration on Earth (m/s²).
    #[pymodule_export]
    pub const GRAVITY: f64 = 9.806_65;

    /// Planck constant (J·s).
    #[pymodule_export]
    pub const PLANCK: f64 = 6.626_070_15e-34;

    /// Speed of light in vacuum (m/s).
    #[pymodule_export]
    pub const SPEED_OF_LIGHT: f64 = 299_792_458.0;

    /// Stefan-Boltzmann constant (W/(m²·K⁴)).
    #[pymodule_export]
    pub const STEFAN_BOLTZMANN: f64 = 5.670_374_419e-08;

    /// Thermodynamic reference temperature (K).
    #[pymodule_export]
    pub const T_REFERENCE: f64 = 298.15;

    /// Normal state reference temperature (K).
    #[pymodule_export]
    pub const T_NORMAL: f64 = 273.15;

    /// Normal state reference pressure (Pa).
    #[pymodule_export]
    pub const P_NORMAL: f64 = 101_325.0;

    /// Get the atomic weight of an element (kg/kmol).
    #[pymodule_export]
    pub use super::elements::get_atomic_weight;
}
