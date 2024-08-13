# SCDL: Single Cell Data Loading for Scalable Training of Single Cell Foundation Models

## Package Overview

SCDL provides an independent pytorch-compatible dataset class for single cell data with a consistent API.
It improves upon simple AnnData-based dataset classes in the following ways:

- A consistent API across input formats that is promised to be consistent across package versions.
- Improved performance when loading large datasets.
- [Future] Full support for ragged arrays (i.e., datasets with different feature counts; currently only a subset of the API functionality is supported for ragged arrays).
- Ability to use datasets that are much, much larger than memory.
- [Future] Support for improved compression.

SCDL's API resembles that of AnnData, so code changes are minimal.
In most places a simple swap from an attribute to a function is sufficient (i.e., swapping `data.n_obs` for `data.number_of_rows()`).

## Installation

SCDL is available as an independent `pip` package from the local source tree:

```bash
pip install -e .
```

Alternatively, it can be installed with
```bash
pip install bionemo[scdl]
```
## Usage

### Getting example data


Here is how to process an example dataset from CellxGene with ~25,000 cells:

Download "https://datasets.cellxgene.cziscience.com/97e96fb1-8caf-4f08-9174-27308eabd4ea.h5ad" to hdf5s/97e96fb1-8caf-4f08-9174-27308eabd4ea.h5ad

### Loading a single cell dataset from an H5AD file

```python
from bionemo.scdl.io.single_cell_memmap_dataset import SingleCellMemMapDataset

data = SingleCellMemMapDataset("97e_scmm", "hdf5s/97e96fb1-8caf-4f08-9174-27308eabd4ea.h5ad")

```

### Interrogating single cell datasets and exploring the API

```python

data.number_of_rows()
## 25382

data.number_of_variables()
## 34455

data.number_of_values()
## 874536810

data.number_nonzero_values()
## 26947275

```

### Using SCDL datasets in model training

SCDL implements the required functions of the PyTorch Dataset abstract class.
You can use PyTorch-compatible DataLoaders to load batches of data from a SCDL class.

```python
from torch.utils.data import DataLoader

## Mock model: you can remove this and pass the batch to your own model in actual code.
model = lambda x : x

dataloader = DataLoader(data, batch_size=8, shuffle=True)
n_epochs = 2
for e in range(n_epochs):
    for batch in dataloader:
        model(batch)
```

### Saving SCDL datasets to disk

When you open a SCDL dataset, you *must* choose a path where the backing
data structures are stored. However, these structures are not guaranteed
to be in a valid serialized state during runtime.

Calling the `save` method guarantees the on-disk object is in a valid serialized
state, at which point the current python process can exit and the object can be
loaded by another process later.

```python

data.save()

```

### Loading SCDL datasets from a SCDL archive

When you're ready to reload a SCDL dataset, just pass the path to the serialized
data:

```python
reloaded_data = SingleCellMemMapDataset("97e_scmm")
```

## Examples

The examples directory contains various examples for utilizing SCDL.

### Converting existing Cell x Gene data to SCDL

To convert existing AnnData files from CellxGene, you can either write your own
script using the SCDL API or utilize the convenience script in `scripts/convert_h5ad_to_scdl.py`.

This script crawls the filesystem to recursively find AnnData files (with the h5ad extension) and converts them to a single SCMMAP. Here's an example:

```bash
python scripts/convert_h5ad_to_scdl.py --data-path hdf5s --save-path example_dataset
```

## Future Work and Roadmap

SCDL is currently in public beta. In the future, expect improvements in data compression
and data loading performance.

## LICENSE

See LICENSE/license.txt.