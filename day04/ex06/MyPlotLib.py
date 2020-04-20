import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MyPlotLib:
    def histogram(self, df, features):
        df[features].hist()
        plt.show()

    def density(self, df, features):
        df[features].plot.kde()
        plt.show()

    def pair_plot(self, df, features):
        sns.pairplot(df[features], markers=".", height=2, plot_kws=dict(linewidth=0))
        plt.show()

    def box_plot(self, df, features):
        sns.boxplot(data=df[features])
        plt.show()
