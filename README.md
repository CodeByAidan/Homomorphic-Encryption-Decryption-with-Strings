# Homomorphic-Encryption-Decryption-with-Strings

This repository contains an [updated version of the original code](https://github.com/bit-ml/he-scheme) by Mădălina Bolboceanu ([@mbolboceanu](https://github.com/mbolboceanu)), Miruna Roșca ([@MirunaRosca](https://github.com/MirunaRosca)), and Radu Țițiu ([@rtitiu](https://github.com/rtitiu)).

## Overview

This code demonstrates an updated version of a homomorphic encryption/decryption scheme. It allows you to perform operations on encrypted data while preserving privacy.

## Getting Started

### Prerequisites

- Python 3.6 or higher is required.
- Ensure you have the necessary dependencies installed. You can install them using `pip` and the `requirements.txt` file.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/CodeByAidan/Homomorphic-Encryption-Decryption-with-Strings.git
   cd Homomorphic-Encryption-Decryption-with-Strings
   ```

2. Install the required dependencies using the provided `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the `main.py` script to see an example usage of the updated homomorphic encryption/decryption scheme:
```bash
python main.py
```

The script demonstrates encryption, decryption, and operations on encrypted data using the "updated scheme".

## API

### Dockerfile (Two Commands!)

Go to [api/](api/) folder, open up [Docker Desktop](https://www.docker.com/products/docker-desktop/). Then build the Dockerfile image into a container:

```bash
cd api/
docker build -t homomorphic-encryption-api .
```

Then run it!

```bash
docker run homomorphic-encryption-api:latest
```

### Sockets - Python (Two Commands!)

Go to [api/](api/) folder (in 2 different terminals), on one run the [`server.py`](api/server.py):

```bash
cd api/
python server.py
```

Then on the other run the [`client.py`](api/client.py):

```bash
python client.py
```

## Additional Resources

For a deeper understanding of the concepts and techniques used in this code, you can refer to the associated research paper: [Paper.pdf](Paper.pdf) as well as the original blogpost about this: https://bit-ml.github.io/blog/post/homomorphic-encryption-toy-implementation-in-python/

