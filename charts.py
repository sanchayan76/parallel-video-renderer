"""
Charts Module
Creates interactive visualizations using Plotly
"""

import plotly.graph_objects as go


def create_comparison_chart(seq_time, par_time):
    """
    Create a bar chart comparing sequential vs parallel processing times
    
    Args:
        seq_time (float): Sequential processing time in seconds
        par_time (float): Parallel processing time in seconds
        
    Returns:
        plotly.graph_objects.Figure: Comparison chart
    """
    fig = go.Figure()
    
    # Sequential bar
    fig.add_trace(go.Bar(
        name='Sequential',
        x=['Sequential', 'Parallel'],
        y=[seq_time, 0],
        marker=dict(
            color='rgba(100, 100, 100, 0.4)',
            line=dict(color='rgba(150, 150, 150, 0.6)', width=1)
        ),
        text=[f'{seq_time:.2f}s', ''],
        textposition='outside',
        textfont=dict(size=14, color='#ffffff'),
        width=0.5
    ))
    
    # Parallel bar
    fig.add_trace(go.Bar(
        name='Parallel',
        x=['Sequential', 'Parallel'],
        y=[0, par_time],
        marker=dict(
            color='rgba(0, 255, 0, 0.4)',
            line=dict(color='rgba(0, 255, 0, 0.6)', width=1)
        ),
        text=['', f'{par_time:.2f}s'],
        textposition='outside',
        textfont=dict(size=14, color='#00ff00'),
        width=0.5
    ))
    
    # Layout
    fig.update_layout(
        title=None,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#a0a0a0', size=12),
        showlegend=False,
        yaxis=dict(
            title='Time (seconds)',
            gridcolor='rgba(255, 255, 255, 0.05)',
            color='#888888',
            title_font=dict(size=11)
        ),
        xaxis=dict(
            color='#888888',
            tickfont=dict(size=12)
        ),
        margin=dict(t=20, b=40, l=50, r=20),
        height=350
    )
    
    return fig


def create_speedup_visualization(speedup):
    """
    Create a visualization showing speedup factor
    
    Args:
        speedup (float): Speedup multiplier (seq_time / par_time)
        
    Returns:
        plotly.graph_objects.Figure: Speedup visualization
    """
    fig = go.Figure()
    
    # Time saved bar
    fig.add_trace(go.Bar(
        name='Time Saved',
        x=[100],
        y=[''],
        orientation='h',
        marker=dict(
            color='rgba(0, 150, 255, 0.5)',
            line=dict(color='rgba(0, 150, 255, 0.6)', width=1)
        ),
        width=0.6,
        showlegend=False
    ))
    
    # Parallel time bar
    fig.add_trace(go.Bar(
        name='Parallel Time',
        x=[100 / speedup if speedup > 0 else 50],
        y=[''],
        orientation='h',
        marker=dict(
            color='rgba(0, 255, 0, 0.5)',
            line=dict(color='rgba(0, 255, 0, 0.6)', width=1)
        ),
        width=0.6,
        showlegend=False
    ))
    
    # Layout with speedup annotation
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': '#a0a0a0', 'size': 12},
        height=350,
        barmode='stack',
        xaxis=dict(
            showgrid=False,
            showticklabels=False,
            range=[0, 100]
        ),
        yaxis=dict(
            showgrid=False,
            showticklabels=False
        ),
        margin=dict(t=80, b=20, l=20, r=20),
        annotations=[
            dict(
                text=f"<b>{speedup:.2f}x</b><br>SPEEDUP",
                x=0.5,
                y=0.85,
                xref='paper',
                yref='paper',
                showarrow=False,
                font=dict(size=32, color='#ffffff'),
                align='center'
            )
        ]
    )
    
    return fig


def create_segment_timeline(num_segments):
    """
    Create a visual timeline showing video segments
    
    Args:
        num_segments (int): Number of video segments
        
    Returns:
        plotly.graph_objects.Figure: Segment timeline visualization
    """
    fig = go.Figure()
    
    # Add line for each segment
    for i in range(num_segments):
        fig.add_trace(go.Scatter(
            x=[i, i+1],
            y=[0, 0],
            mode='lines+markers',
            line=dict(color='#00ff00', width=10),
            marker=dict(size=15, color='#00ff00', symbol='circle'),
            name=f'Segment {i+1}',
            showlegend=False
        ))
    
    # Layout
    fig.update_layout(
        title=f'Video Split into {num_segments} Segments',
        title_font=dict(size=18, color='#00ff00'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#00ff00'),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        xaxis=dict(
            title='Segment Number',
            gridcolor='rgba(0, 255, 0, 0.1)',
            color='#00ff00'
        ),
        height=200
    )
    
    return fig
