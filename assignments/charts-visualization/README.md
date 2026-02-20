# 📘 Assignment: Building Beautiful Charts with Charts Framework

## 🎯 Objective

Learn to create professional and visually appealing data visualizations using a Charts framework. You'll build interactive charts to represent different types of data and understand how to communicate data insights effectively through visualization.

## 📝 Tasks

### 🛠️ Set Up Charts Framework and Create Basic Charts

#### Description
Initialize your charting environment and create your first basic chart types including line, bar, and pie charts to visualize simple datasets.

#### Requirements
Completed program should:

- Import the Charts framework correctly
- Create at least three different chart types (line, bar, and pie)
- Use provided sample datasets for each chart
- Configure chart labels and titles appropriately
- Display charts in a window or export them as images
- Include proper comments explaining chart setup

Example chart creation:
```python
# Bar chart example
chart = BarChart()
chart.title = "Sales by Quarter"
chart.add_data(["Q1", "Q2", "Q3", "Q4"], [100, 150, 200, 175])
chart.display()
```

### 🛠️ Customize Chart Appearance and Styling

#### Description
Enhance your charts with custom colors, fonts, legends, and other styling options to make them visually appealing and professional.

#### Requirements
Completed program should:

- Apply custom color schemes to charts
- Configure fonts and font sizes for readability
- Add legends to identify data series
- Use grid lines and axes labels effectively
- Apply styling consistent across multiple charts
- Test different color palettes for accessibility

Example customization:
```python
chart.colors = ["#FF6B6B", "#4ECDC4", "#45B7D1"]
chart.legend_position = "bottom"
chart.font_size = 12
```

### 🛠️ Create Multi-Series Charts and Interactive Features

#### Description
Build more complex visualizations with multiple data series and add interactive features like tooltips, zoom, and drill-down capabilities where supported.

#### Requirements
Completed program should:

- Create charts with multiple data series
- Add tooltips showing detailed information on hover
- Implement zoom and pan functionality if supported
- Include comparative charts side-by-side
- Handle large datasets efficiently
- Export charts in multiple formats (PNG, SVG, or interactive HTML)
