# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: .w2053761......# Date: ..2023/12/13............

#import graphics file
from graphics import *

#main histrogram function
def graph(progress_result_list):
    graphics_window = GraphWin("Histogram results", 800,600)#create graphics window
    graphics_window.setCoords(0,0,800,600)
    #calculate results count
    progress_frequency = progress_result_list.count("Progress")
    trailer_frequency = progress_result_list.count("Progress-module trailer")
    retriever_frequency = progress_result_list.count("Do not Progress - module retriever")
    exclude_frequency = progress_result_list.count("Exclude")

    list = [progress_frequency , trailer_frequency , retriever_frequency , exclude_frequency]
    maximum_height = max(list)#assing maximum height to list
    if maximum_height == 0:       
       return
    scale = 400 / maximum_height

    # main heading
    text = Text(Point(220,560), "Histogram results")
    text.setSize(23)
    text.setFill("gray")
    text.setFace("helvetica")
    text.setStyle("bold")
    text.draw(graphics_window)


    # creating rectangles
    def rectangle():
        rectangle1 = Rectangle(Point(100,100),Point(200,(100 +list[0] * scale)))
        rectangle2 = Rectangle(Point(220,100),Point(320,(100 + list[1] * scale)))
        rectangle3 = Rectangle(Point(340,100),Point(440,(100 + list[2] * scale)))
        rectangle4 = Rectangle(Point(460,100),Point(560,(100 + list[3] * scale)))

        # Drawing rectangles
        rectangle1.setFill("pale green") 
        rectangle1.setOutline("lightsteelblue4")  
        rectangle2.setFill("darkolivegreen3")  
        rectangle2.setOutline("lightsteelblue4")
        rectangle3.setFill("chartreuse3")
        rectangle3.setOutline("lightsteelblue4")
        rectangle4.setFill("lightpink2")
        rectangle4.setOutline("lightsteelblue4")
        return rectangle1.draw(graphics_window), rectangle2.draw(graphics_window), rectangle3.draw(graphics_window), rectangle4.draw(graphics_window)

    # creating the line
    def creating_bar():
        line = Line(Point(80,100),Point(580,100))
        line.setFill("lightsteelblue4")#set the colour for line
        return line.draw(graphics_window)

    def creating_labels():
    # creating progress label
        progress_label = Text(Point(150,80), "Progress")    
        progress_label.setFill("lightsteelblue4")#set the colour for progresslable
        progress_label.setSize(14)#set size
        progress_label.setStyle("bold")    

        # creating trailer label
        trailer_label = Text(Point(270,80), "Trailer")
        trailer_label.setFill("lightsteelblue4")
        trailer_label.setSize(14)
        trailer_label.setStyle("bold")
        
        # creating retriever label
        retriever_label = Text(Point(390,80), "Retriever")
        retriever_label.setFill("lightsteelblue4")
        retriever_label.setSize(14)
        retriever_label.setStyle("bold")
        retriever_label.setOutline("lightsteelblue4")

        # creating exclude label
        excluded_label = Text(Point(510,80), "Excluded")
        excluded_label.setFill("lightsteelblue4")
        excluded_label.setSize(14)
        excluded_label.setStyle("bold")
        excluded_label.setOutline("lightsteelblue4")

        return progress_label.draw(graphics_window), trailer_label.draw(graphics_window), retriever_label.draw(graphics_window), excluded_label.draw(graphics_window)
    #label function
    def counts():
        progress_label = Text(Point(150,(100 +list[0] * scale)+20), progress_frequency)
        progress_label.setFill("lightsteelblue4")
        progress_label.setSize(16)
        progress_label.setStyle("bold")

        # creating trailer label
        trailer_label = Text(Point(270,(100 + list[1] * scale)+20), trailer_frequency)
        trailer_label.setFill("lightsteelblue4")
        trailer_label.setSize(16)
        trailer_label.setStyle("bold")
        
        # creating retriever label
        retriever_label = Text(Point(390,(100 + list[2] * scale)+20), retriever_frequency)
        retriever_label.setFill("lightsteelblue4")
        retriever_label.setSize(16)
        retriever_label.setStyle("bold")

        # creating exclude label
        excluded_label = Text(Point(510,(100 + list[3] * scale)+20), exclude_frequency)
        excluded_label.setFill("lightsteelblue4")
        excluded_label.setSize(16)
        excluded_label.setStyle("bold")

        return progress_label.draw(graphics_window), trailer_label.draw(graphics_window), retriever_label.draw(graphics_window), excluded_label.draw(graphics_window)
    #calculate the total results
    def total_count():
        total = sum(list)
        total_count = Text(Point(230,40), f"{total} Outcomes in Total")
        total_count.setFill("lightsteelblue4")
        total_count.setSize(19)
        total_count.setStyle("bold")
        total_count.setOutline("lightsteelblue4")
        return total_count.draw(graphics_window)
    #call functions
    rectangle()
    creating_bar()
    creating_labels()
    counts()
    total_count()
    
    try:
        graphics_window.getMouse()
        graphics_window.close()
    except:
        print("window closed")#if window close by cross sign avoid error massage 

