import xml.etree.ElementTree as ET
import xml.dom.minidom as md
from Coaster import Coaster
from PI import PI


class Cheers:
    """
    A class that represents a coaster simulation and analysis system.

    Attributes
    ----------
    coaster1 : object
        an instance of the Coaster class that represents the coaster
    x0 : float
        the starting point for Newton's method

    Methods
    -------
    get_input():
        Method to get input from the user for the coaster simulation

    get_newton_input():
        Method to get the starting point for Newton's method from the user

    display_output():
        Method to display the simulation output in a string format

    run():
        Method to run the simulation
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the CHEERS object.
        """
        self.coaster1 = None
        self.x0 = PI()/2

    def get_input(self):
        """
        Method to get input from the user for the coaster simulation.
        """
        radius_1 = float(input('Enter the radius of coaster: '))
        self.coaster1 = Coaster(radius_1)

    def get_newton_input(self):
        """
        Method to get the starting point for Newton's method from the user.
        """
        self.x0 = float(input('Enter the starting point for newton method: '))

    def display_output(self):
        """
        Method to display the simulation output in a string format.

        Returns
        -------
        string
            A formatted string that represents the simulation output.
        """
        string = ''
        string += f'{self.coaster1.display()}\t'
        string += f'{self.coaster1.overlap()}\t'
        string += f'{self.coaster1.shift_distance(self.x0)}'
        return string

    def run(self):
        """
        Method to run the simulation.

        Returns
        -------
        tuple
            A tuple containing the radius of the coaster and the simulation output.

        Raises
        ------
        ValueError
            If the input value for radius is invalid, it raises an exception.
            If the input value for starting point is invalid, it raises an exception.
        """
        while True:
            try:
                self.get_input()
                break
            except ValueError:
                print('Invalid input. Please enter a valid value for Radius.')
        while True:
            try:
                self.get_newton_input()
                return self.display_output()
            except ValueError:
                print('Invalid input. Please enter a valid starting point for newton method.')

    def to_xml(self,root,index,result_arr):
        """Convert the result to xml format
        Args:
            root :root element of the xml
            index (int): coaster's name
            result (String): The ouput of the coaster obtained 

        Returns:
            root: root element of the xml
        """
        coaster_no = ET.SubElement(root, 'coaster', name=str(index))
        radius = ET.SubElement(coaster_no, 'radius')
        radius.text = result_arr[0]
        area = ET.SubElement(coaster_no, 'area')
        area.text = result_arr[1]
        circum = ET.SubElement(coaster_no, 'circumference')
        circum.text = result_arr[2]
        overlap = ET.SubElement(coaster_no, 'overlapArea')
        overlap.text = result_arr[3]
        distance=ET.SubElement(coaster_no,'distancetoshift')
        distance.text=result_arr[4]
        return root

if __name__ == '__main__':
    """
    The main function that runs the CHEERS program.
    """
    cheers = Cheers()
    S = 1
    index = 1
    root = ET.Element('cheers')
    while S != 0:
        cheers = Cheers()
        result = cheers.run()
        result_arr=result.split('\t')
        print('overlap_area: ',result_arr[3])
        print('Distance to Shift: ',result_arr[4])
        root = cheers.to_xml(root,index,result_arr)
        index += 1
        while True:
            try:
                S = int(input('Do you wish to continue?Press any number or Press 0 to exit\n'))
                break
            except ValueError:
                print('Enter a valid number to continue or exit')
    xml_output = ET.tostring(root).decode('utf-8')
    dom = md.parseString(xml_output)
    output = dom.toprettyxml(indent='\t')
    with open('result.xml', 'w') as f:
        f.write(output)
