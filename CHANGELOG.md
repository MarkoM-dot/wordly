## v0.2.2 (2025-08-07)

### Fix

- **cli**: ensure connections get closed after requesting definitions from server (#11)

## v0.2.1 (2025-04-20)

### Fix

- **ci**: make use of uv when running commands (#3)

## v0.2.0 (2025-04-20)

### Feat

- **wordly**: add automated deploy and additional documentation information

## v0.1.4 (2025-04-19)

### Refactor

- **ci**: remove token from ci in favor of trusted publishing implementation

## v0.1.3 (2025-04-19)

## v0.1.2 (2025-04-19)

### Fix

- **ci**: set attestations to false

## v0.1.1 (2025-04-19)

### Feat

- **ci**: test against multiple python versions

## v0.1.0 (2025-04-18)

### Feat

- **wordly**: test first working version
- **ci**: run tests on push to main pr to main

### Fix

- **tests**: ensure bytearray is in the tests

### Refactor

- **parser**: make use of bytearray instead of sting conversions
- **status**: ensure all members of the enum are bytes

## v0.0.3 (2024-09-28)

### Feat

- **make**: add helpful commands to check build
- **docs**: provide module information
- **project**: supports python3.11, point to issues, and provide additional topic information

### Fix

- **tests**: rename test file

## v0.0.2 (2024-09-28)

### Feat

- **release**: prepare for new release
- **docs**: provide more information on package usage

### Fix

- **build**: ensure dynamic versioning
- **docs**: fix stray gt sign
- **docs**: get rid of rst
