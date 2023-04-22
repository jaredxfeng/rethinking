Statistical rethinking is an introductory course on Bayesian data analysis and causal inference, offered by Richard McElreath. 

The course is accompanied by a [textbook](https://xcelab.net/rm/statistical-rethinking/), a yearly [lecture series](https://youtu.be/FdnMWdICdRs) and [repo](https://github.com/rmcelreath/stat_rethinking_2023), another [accompanying repo](https://github.com/rmcelreath/rethinking) that has all the R code, and some community resources that translate the code to other languages & libraries. 

Specifically, there is a rather complete [PyMC translation](https://github.com/pymc-devs/pymc-resources/tree/main/Rethinking_2) created by the community. However, upon an initial run of some of those notebooks, I found a lot of outdated stuff, such as deprecated functions, and even deprecated supporting packages. A lot of the code there might not be reusable since PyMC has changed over the years. Hence, here I have been working on a new PyMC translation that reflects the latest version (v5). The first half of the course mainly uses quadratic approximation to do approximate Bayesian inference, which the PyMC repo didn't attempt to replicate (shame on them), so I had to bring in non-PyMC code such as Numpyro, and I even implemented a simple `pyquap` with `scipy.optimize.minimize` and `autograd` (which didn't go too far beyond estimating the mean and variance of a variable).

I am rolling out the jupyter notebooks chapter by chapter, with an aim for completeness (should include the majority of the code from the original book) and coherency (the code & other contents should be mostly self-explanatory). 

# Display notebooks
[<img src="https://nbviewer.org/static/img/nav_logo.svg" width="150"/>](https://nbviewer.org/github/jaredxfeng/rethinking/tree/dev/).

# Goodnotes
And here are some [goodnotes](https://web.goodnotes.com/s/8ERStxgngckNf2VWF4FujP#page-1) I have been taking when listening to the 2023 lectures. Again I skipped the first few chapters there, and they tend to be way ahead of the jupyter notebooks.

# Numpyro dependencies
Before installing Numpyro and its dependencies, you should install all `Pipfile` dependencies by doing `pipenv install` in the repo root, immediately after cloning this repo.

If you plan to use CPU, you are recommended to do `pipenv install numpyro` directly. That way, jax and jaxlib (cpu versions) would be automatically installed as well, but might run into compatibility issues between jax and jaxlib, and you will need to resolve those by manually upgrading jax and/or jaxlib.

If you plan to use GPU, you cannot use `pipenv` commands anymore, because it cannot parse `pip install` options such as `--upgrade` or `-f` which are necessary for installing GPU versions of jax. You could either (1) install CUDA, install cuDNN, and finally do `pip install` in your activated venv per jax's official guide, or (2) install the jax and jaxlib bundled with CUDA and cuDNN. Please refer to [jax repo's readme](https://github.com/google/jax) for a complete guide. After completing either steps, you can install Numpyro. 

Final notes for GPU users: 
- If you are a regular PyTorch user, note that PyTorch automatically bundles CUDA and cuDNN. But that's not what jax always does, and you might have to install CUDA and cuDNN separately.
- Upgrading your NVIDIA driver to the latest version is recommended before installing CUDA and cuDNN. Or you will have to carefully select CUDA and cuDNN versions according to your current NVIDIA driver version. Please consult NVIDIA's official documentations.
- If you are a experienced jax user and you have your own approach to build things up, you might as well ignore instructions here.

