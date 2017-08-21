# envloader

A simple CLI to loads environment variables into a local db

## Installation

```bash
# Install with pip
sudo pip install git+https://github.com/fivepapertigers/envloader.git@master
# Run initialization
envloader init
```

Add the following line to your `~/.bash_profile`:

```bash
alias envloader='source envloader'
```

## Usage

Store a new environment variable:

```
envloader store
```


Find and load environment variables:

```
envloader load
```