# TSGen.Check

A tool made to check the validity of Thunderstore required files.

Checks:

- Manifest:
  - All required fields are present
  - Name follows proper regex ([a-zA-Z0-9_])
  - Version number follows [Semantic Versioning](https://semver.org).
  - Description is under 250 characters
  - Dependencies are in list format
- Icon
  - Has a size of 256x256
- Readme
  - Is present

## Installation/Usage

1. Download `TSGen.Check.exe` from the [Releases](https://github.com/nayr31/TSGen.Check/releases) page.
2. Place it in a folder next to your files you wish to check.
3. Run the program and follow the terminal prompts.
