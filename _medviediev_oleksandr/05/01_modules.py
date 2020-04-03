'''
import package.my_module


package.my_module.show_this('My file')
'''
'''
from package import my_module


my_module.show_this('My file')
'''
from package.my_module import show_this


show_this('My file')
