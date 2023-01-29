from Spotfire.Dxp.Application.Visuals import VisualContent, VisualTypeIdentifiers
from System.Drawing import * 

font = Font("Roboto",7) # Set your desired font style and size here

# Get the active page
page = Application.Document.ActivePageReference

# Iterate through all visualizations on the page
for vis in page.Visuals:
	# Get the visual content object
	visContent = vis.As[VisualContent]()
	# Change fonts for core plots
	if vis.TypeId in [VisualTypeIdentifiers.BarChart, VisualTypeIdentifiers.ScatterPlot, VisualTypeIdentifiers.LineChart, VisualTypeIdentifiers.CombinationChart, VisualTypeIdentifiers.HeatMap, VisualTypeIdentifiers.ParallelCoordinatePlot]:
		visContent.LabelFont = font
		visContent.XAxis.Scale.Font = font
		visContent.YAxis.Scale.Font = font
		visContent.Legend.Font = font
	
	# Change fonts for Pie chart
	if vis.TypeId in [VisualTypeIdentifiers.PieChart]:
		visContent.VisualAttributes.LabelFont = font
		visContent.Legend.Font = font

	# Change fonts for Tables
	if vis.TypeId in [VisualTypeIdentifiers.Table, VisualTypeIdentifiers.SummaryTable]:
		visContent.TableFont = font
		visContent.TableHeaderFont = font
		visContent.Legend.Font = font