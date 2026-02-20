"""
Building Beautiful Charts with Charts Framework - Starter Code

This is a starter template for creating visualizations with a charting library.
Follow the assignment requirements to implement the missing functionality.
"""

# TODO: Import the appropriate charting library
# Examples: matplotlib, plotly, bokeh, or another charts framework
# import matplotlib.pyplot as plt
# OR
# from plotly import express as px


# TODO: Load sample data or create sample datasets
# Example dataset structure
sample_data = {
    "quarterly_sales": {
        "labels": ["Q1", "Q2", "Q3", "Q4"],
        "values": [45000, 52000, 48500, 61000]
    },
    "product_distribution": {
        "labels": ["Product A", "Product B", "Product C", "Product D"],
        "values": [30, 25, 20, 25]
    },
    "monthly_trend": {
        "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "sales": [15000, 18000, 16500, 21000, 23000, 25000],
        "expenses": [10000, 11000, 10500, 12000, 13000, 14000]
    }
}


# TODO: Task 1 - Create basic chart types
def create_bar_chart():
    """Create a bar chart from sample data"""
    # IMPLEMENT: Create a bar chart using quarterly_sales data
    # Include proper title and axis labels
    pass


def create_pie_chart():
    """Create a pie chart from sample data"""
    # IMPLEMENT: Create a pie chart using product_distribution data
    # Include proper title and legend
    pass


def create_line_chart():
    """Create a line chart from sample data"""
    # IMPLEMENT: Create a line chart showing monthly_trend data
    # Include proper title, axis labels, and legend
    pass


# TODO: Task 2 - Customize chart styling
def apply_custom_styling(chart):
    """Apply custom colors and styling to a chart"""
    # IMPLEMENT: Define custom color palette
    custom_colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]
    
    # IMPLEMENT: Apply colors to the chart
    
    # IMPLEMENT: Configure font sizes and styles
    
    # IMPLEMENT: Add grid lines and improve readability
    pass


# TODO: Task 3 - Create multi-series chart
def create_multi_series_chart():
    """Create a chart with multiple data series"""
    # IMPLEMENT: Create a chart comparing sales and expenses
    # Use monthly_trend data with multiple series
    # Add legend to differentiate between series
    pass


# TODO: Main function to display all charts
def main():
    """Generate and display all charts"""
    print("Creating basic charts...")
    create_bar_chart()
    create_pie_chart()
    create_line_chart()
    
    print("Creating styled charts...")
    create_multi_series_chart()
    
    print("All charts created successfully!")
    # IMPLEMENT: Display charts or save them to files


if __name__ == "__main__":
    main()
