OK. No counterpart in PyMC for quadratic approximation (shame). No easy DIY replicate for that too 
(see the backup section of chapter 4 notebook for how that failed miserably). 

Had to use Numpyro's `SVI` algorithm (variational inference) for a more advanced version of quadratic approximation. 
Saw some people on the Internet said that the two approaches are quite similar.

#### But what's the difference between classic quadratic approximation and variational inference with Gaussian proxies?

In short, classic quadratic approximation finds the argmax of the true posterior (given an adequately powerful optimizer), 
and then the 2nd order curvature locally at that argmax would become the inverted covariance matrix. The true posterior gradient w.r.t. the latent variables is zero.

On the other hand,
the variational parameters of the Gaussian VI approach would converge to a point 
where the true posterior gradient w.r.t the latent variables is zero _on average_, with expectation taken over the learned approximate Gaussian distribution.
Similar conclusions for the covariance matrix. 

#### References

[The Variational Gaussian Approximation
Revisited](http://www0.cs.ucl.ac.uk/staff/c.archambeau/publ/neco_mo09_web.pdf) by Opper et al (2009). 
Section 2 formally described the similarity between Gaussian VI and quadratic (Laplace) approximation.

[A practical tutorial on Variational Bayes](https://arxiv.org/abs/2103.01327) by Tran et al (2021). Some more general notes about VI.
