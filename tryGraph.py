import plotly.graph_objs as go

# Example data
words = ['English', 'Mandarin', 'Hindi', 'Spanish', 'French']
population = [1132, 1117, 615, 534, 280]

# Create a bar chart
fig = go.Figure([go.Bar(x=words, y=population)])

# Update layout
fig.update_layout(title='Word Population',
                  xaxis_title='Word',
                  yaxis_title='Population')

# Show the plot
fig.show()