# TSGen.Check

A tool made to check the validity of Thunderstore manifests on a basic level.

Checks:

- All required fields are present
- Name follows proper regex ([a-zA-Z0-9_])
- Version number is a 3 length string of dots
- Description is under 250 characters
- Dependencies are in list format

## Installation/Usage

1. Download `TSGen.Check.exe` from the [Releases](https://github.com/nayr31/TSGen.Check/releases) page. 
2. Place it in a folder next to your `manifest.json` file you wish to check.
3. Run the program and follow the terminal prompts.
