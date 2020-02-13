from sklearn.datasets import  load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


iris = load_iris()
print(iris.keys())

n_samples,n_features=iris.data.shape
print(n_samples,n_features)
iris.data[0:5]

print(iris.target.shape)
print(iris.target_names)
iris.target

iris_data = pd.DataFrame(iris.data,columns= iris.feature_names)
iris_data['species'] = iris.target_names[iris.target]
iris_data.head(3).append(iris_data.tail(3))

sns.pairplot( iris_data,hue='species', palette='husl' )
plt.show()