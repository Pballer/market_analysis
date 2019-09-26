"""Module for plotting results."""

def plot_prediction(tic_predict, tic):
    aapl_pred = tic_predict.loc[tic_predict.tic == tic].copy()
    aapl_pred = aapl_pred.set_index('date').sort_index()
    ax = aapl_pred.open.plot.line(figsize=(15,10))
    
    for pred in aapl_pred.loc[aapl_pred.predicted_class == 'loss'].index:
        ax.axvline(pred, c='red')

    for pred in aapl_pred.loc[aapl_pred.predicted_class == 'gain'].index:
        ax.axvline(pred, c='green')

    ax.set_title('{} Predictions'.format(tic))
    ax.set_ylabel('Stock Price')
    ax.set_xlabel('Date')

    red_patch = mpatches.Patch(color='red', label='Predicted Loss')
    green_patch = mpatches.Patch(color='green', label='Predicted Gain')
    plt.legend(handles=[red_patch, green_patch])

    plt.savefig('../visualizations/{}_prediction.png'.format(tic), transparent=True)

