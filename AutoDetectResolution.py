# Neil Kanungo
# TIBCO Software
# January 2023
# Auto Detect Screen Resolution and switch/hide pages

# Get Screen Resolution
pageSize = Document.ActivePageReference.GetVisualizationAreaSize()

# Set Limits and Identifiers
mobileWidth = 600
tabletWidth = 1280
mobileID = '[M]'
tabletID = '[T]'

# Hide/Switch pages depending on Screen Resolution Width
if (pageSize.Width > tabletWidth):  # Full Size Condition
	Document.ActivePageReference = Document.Pages[0]
	for p in Document.Pages:
		if ((p.Title.find(mobileID)>0) or (p.Title.find(tabletID)>0)):
			p.Visible = False
		else:
			p.Visible = True

elif (pageSize.Width <= tabletWidth and pageSize.Width > mobileWidth):   # Tablet Size Condition
	Document.ActivePageReference = Document.Pages[1]
	for p in Document.Pages:
		if (p.Title.find(tabletID)>0):
			p.Visible = True
		else:
			p.Visible = False

else:  # Mobile Size Condition
	Document.ActivePageReference = Document.Pages[2]
	for p in Document.Pages:
		if (p.Title.find(mobileID)>0):
			p.Visible = True
		else:
			p.Visible = False
