from yellowbrick.features import Rank2D
from sklearn.svm import LinearSVC
from yellowbrick.classifier import ROCAUC
from yellowbrick.features import JointPlotVisualizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot
from yellowbrick.regressor import AlphaSelection
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import Ridge

from yellowbrick.regressor import PredictionError
import pandas as pd
import numpy  as np



def testFunc5(savepath ='Results/bikeshare_Rank2D.png'):
    '''
    共享单车数据集预测
    '''
    data = pd.read_csv('fixtures/bikeshare/bikeshare.csv')
    X = data[["season","month","hour","holiday","weekday","workingday","weather","temp","feelslike","humidity","windspeed"]]
    Y = data["riders"]

    visualizer = Rank2D(algorithm="pearson")
    visualizer.fit_transform(X)
    visualizer.poof(outpath=savepath)

def testFunc6(savepath ='Results/bikeshare_temperate_feelslike_relation.png'):
    '''
    进一步考察相关性
    '''
    data = pd.read_csv('fixtures/bikeshare/bikeshare.csv')

    X = data[["season","month","hour","holiday","weekday","workingday","weather","temp","feelslike","humidity","windspeed"]]
    Y = data["riders"]

    visualizer = JointPlotVisualizer(feature ='tmp',target='feelslike')
    visualizer.fit(X['temp'],X['feelslike'])
    visualizer.poof(outpath=savepath)


def testFunc7(savepath ='Results/bikeshare_LinearRegression_ResidualsPlot.png'):
    '''
    基于共享单车数据使用线性回归模型预测
    '''
    data = pd.read_csv('fixtures/bikeshare/bikeshare.csv')
    X = data[["season","month","hour","holiday","weekday","workingday","weather","temp","feelslike","humidity","windspeed"]]
    Y = data["riders"]
    X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3)
    visualizer = ResidualsPlot(LinearRegression())
    visualizer.fit(X_test,y_test)
    visualizer.poof(outpath=savepath)

def testFunc8(savepath ='Results/bikeshare_RidgeCV_AlphaSelection.png'):
    '''
    基于共享单车数据使用AlphaSelection
    '''
    data = pd.read_csv('fixtures/bikeshare/bikeshare.csv')
    X = data[["season","month","hour","holiday","weekday","workingday","weather","temp","feelslike","humidity","windspeed"]]
    Y = data["riders"]
    alphas = np.logspace(-10,1,200)
    visualizer  = AlphaSelection(RidgeCV(alphas = alphas))
    visualizer.fit(X,Y)
    visualizer.poof(outpath=savepath)


def testFunc9(savepath ='Results/bikeshare_Ridge_PredictionError.png'):
    '''
    基于共享单车数据使用AlphaSelection
    '''
    data = pd.read_csv('fixtures/bikeshare/bikeshare.csv')
    X = data[["season","month","hour","holiday","weekday","workingday","weather","temp","feelslike","humidity","windspeed"]]
    Y = data["riders"]

    X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3)
    visualizer = PredictionError(Ridge(alpha=3.181))
    visualizer.fit(X_train,y_train)
    visualizer.score(X_test,y_test)
    visualizer.poof(outpath=savepath)


if __name__ == '__main__':
    testFunc9()
