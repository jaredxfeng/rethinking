Statistical rethinking is an introductory course on Bayesian data analysis and causal inference, offered by Richard McElreath. 

The course is accompanied by a [textbook](https://xcelab.net/rm/statistical-rethinking/), a yearly [lecture series](https://youtu.be/FdnMWdICdRs) and [repo](https://github.com/rmcelreath/stat_rethinking_2023), another [accompanying repo](https://github.com/rmcelreath/rethinking) that has all the R code, and some community resources that translate the code to other languages & libraries. 

Specifically, there is a rather complete [PyMC translation](https://github.com/pymc-devs/pymc-resources/tree/main/Rethinking_2) created by the community. However, upon an initial run of some of those notebooks, I found a lot of outdated stuff, such as deprecated functions, and even deprecated supporting packages. A lot of the code there might not be reusable since PyMC has changed over the years. Hence, here I have been working on a new PyMC translation that reflects the latest version (v5). The first half of the course mainly uses quadratic approximation to do approximate Bayesian inference, which the PyMC repo didn't attempt to replicate (shame on them), so I had to bring in non-PyMC code such as Numpyro, and I even implemented a simple `pyquap` with `scipy.optimize.minimize` and `autograd` (which didn't go too far beyond estimating the mean and variance of a variable).

I am rolling out the jupyter notebooks chapter by chapter, with an aim for completeness (should include the majority of the code from the original book) and coherency (the code & other contents should be mostly self-explanatory). I am not strictly following the chapter-wise order since I do not value some of the early chapters as high as the remaining ones. 

# Display notebooks
[<img src="https://nbviewer.org/static/img/nav_logo.svg" width="150"/>](https://nbviewer.org/github/jaredxfeng/rethinking/tree/dev/).

# Goodnotes
And here are some [goodnotes](https://web.goodnotes.com/s/8ERStxgngckNf2VWF4FujP#page-1) I have been taking when listening to the 2023 lectures. Again I skipped the first few chapters there, and they tend to be way ahead of the jupyter notebooks.

# Fancy title page from the 2023 course
<img src="title.gif" width="500">