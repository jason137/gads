# kNN classification

training step  
- store (cache) training recs

predicion step  
- for each query point, find distances to all training points  
- assign label by majority vote of k nearest training points (neighbors)

"non parametric"
- closely related to clustering, but here we use label info from training records
    - **supervised** technique

training step consists of just storing the training examples!
- all calculations postponed until prediction time
- tradeoff: no computational complexity incurred here, lots incurred later

since no computations are performed in the training step, this is called a **lazy learner**
- contrast w **eager learner** (eg logistic regression), which commits to
  vector of parameters in training step, for the purpose of generalizing globally

each time a new record is encountered, its distances to training records are determined &
a new **local** hypothesis is created which is valid only for this new record
- one local hypothesis (eg, pointwise classification decision) is not meant to generalize to another point
- **instance-based learner**
- **non-generalizing algorithm**

these models are sensitive to the local structure of the data
- complex **decision boundaries** possible
- high danger of **overfitting**

## what can lead to difficulty?

skewed class distribution
- can overcome by weighting votes eg by (1/distance)^n
- can also help to smooth out predictions when training data is noisy
- allows algo to be run "globally" (pointwise hypotheses borrow info from oher
  points)

complexity from rows
- high computational expense in calculating distances
    - equivalent to saying that kNN is difficult to **scale**
    - distance matrix calc has **quadratic complexity**, eg O(n^2)
    - but it can be parallelized! (why?)

complexity from columns
- if dep variable relies only on a subset of attributes, then distance calcs
  across all attributes can be misleading
    - **feature selection**
- out of scale feature can bias distance calcs
    - **feature scaling**
- NN models are especially susceptible to **curse of dimensionality**
    - can be mitigated by CV
    - note CV w/ NN models is particularly easy, since number of training steps
      is independent of number of folds; eg O(1))

addl preprocessing option: dim reduction or clustering
- eg, could perform PCA & then kNN on **latent features** in lower-dim space

how to choose k?
- large k --> reduce effects of noise --> possible underfitting!
- small k --> achieve complex dec boundaries --> possible overfitting!
- choose k by CV

side note: wouldn't it be nice if your model could help you select a balance
between underfitting & overfitting?
- **bias/variance tradeoff**
- **regularization**

## what do you really need to perform kNN?

a **distance matrix** (equiv, similarity mtx)
- n\*(n-1)/2 calcs (**quadratic complexity**)

clearly this depends heavily on your choice of **metric**
- continuous feature space: usually Euclidean distance
- other feature space (eg docs, strings): Jaccard coeff, cosine distance, tf-idf, Levenshtein distance, etc

applicable to any data that can be embedded in a **metric space**
- tricky part: figuring out metric space embedding
    - probably wrong approach: create a new metric for your problem
    - probably right approach: think about how to use an existing metric
    - Gauss: "think deeply of simple things"

- this matches the implicit classification schemes that our brains apply intuitively!

## what can we say about the hypothesis space of a NN model?

- hyp space forms a **Voronoi tessellation**
    - shape depends on the metric

- lazy learners (like kNN) make local generalizations & avoid forming an explicit global hypothesis
    - complex decision boundaries (higher variance)
    - more susceptible to overfitting than underfitting (lower bias)
    - but still possible to underfit! eg for too-large values of k

- eager learners place more restrictions on their hypothesis spaces
    - ex: logistic regression creates a global **linear decision boundary**
        - less model complexity (lower variance)
        - danger of underfitting (higher bias)
