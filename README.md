# QuantifyX

**Precision in Every Unit**  
_The Krittika Project_

---

## Overview

QuantifyX is a professional-grade computational engine for:

- Mathematical shapes (area, volume, perimeter)
- Weights and measurements
- Dimension and unit conversions
- Engineering-oriented units and constants

This project is designed as a **core calculation layer**, intended to be:
- Testable
- Upgrade-safe
- API-ready
- Web-integration friendly

QuantifyX will later power web applications, engineering tools, and automated workflows.

---

## Design Philosophy

- Pure computation (no UI, no input handling)
- Deterministic and test-driven
- Strong separation of concerns
- Long-term maintainability over quick features

> Build once. Build clean. Let it compound.

---

## Project Structure (High Level)
quantifyx/
├── src/quantifyx/ # Core computation engine
├── tests/ # Unit tests
├── docs/ # Technical documentation
├── examples/ # Usage examples


---

## Technology Stack

- Python (core engine)
- pytest (testing – added early by design)
- Git & GitHub (version control)
- VS Code (development environment)

---

## Roadmap (High Level)

- Phase 1: Geometry & unit conversion core
- Phase 2: Engineering units and constants
- Phase 3: API layer (FastAPI)
- Phase 4: Web UI integration
- Phase 5: Packaging & reuse

---

## Author

**Amaljit Bharali**  
Engineer  
Project under: **The Krittika Project**

---

## License

This project is licensed under the MIT License.

---

## Release History

### v0.2.0
- Complete unit system (length, area, volume, mass, flow, velocity)
- Physics layer (density, pressure, Darcy-Weisbach)
- Colebrook-White solver
- Intelligent friction factor selector
- High-level hydraulics pipe API
- Pipe material roughness database
- 100% tested core modules

Test branch protection setup.