from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton ,MDRectangleFlatIconButton,MDFlatButton
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import pandas
from kivy.uix.label import Label
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, ObjectProperty,NumericProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.core.window import Window


class WindowManager(MDScreenManager):
    pass

class LoginScreen(Screen):
    pass

class ClassesScreen(Screen):
    # menu = ObjectProperty()
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     menu_items = [
    #         {
    #             "viewclass": "OneLineListItem",
    #             "height": 56,
    #             "text": f"Item {i}",
    #         }
    #         for i in range(5)
    #     ]
    #     self.menu = MDDropdownMenu(items=menu_items, width_mult=4)
    # def on_start(self):
    #     for i in range(6):
    #         self.dropdown.items.append({
    #             'viewclass':'MDMenuItem',
    #             'text':'option' + str(i),
    #             'callback':self.option_callback
    #         })
    # def open_menu(self, caller):
    #     self.menu.caller = caller
    #     self.menu.open()

    
    pass
class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, MDFlatButton):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(
            rv, index, data)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected


class QuestionDb(BoxLayout):
    items_list = ObjectProperty(None)
    column_headings = ObjectProperty(None)
    rv_data = ListProperty([])

    def __init__(self, **kwargs):
        super(QuestionDb, self).__init__(**kwargs)
        self.get_dataframe()

    def get_dataframe(self):
        df = pandas.read_excel("Book1.xlsx")

        # Extract and create column headings
        # for heading in df.columns:
        #     self.column_headings.add_widget(Label(text=heading,font_size=30))
        # print(len(df.columns))

        # Extract and create rows
        data = []
        for row in df.itertuples():
            for i in range(1, len(row)):
                data.append([row[i], row[0]])
        self.rv_data = [{'text': str(x[0]), 'Index': str(x[1])} for x in data]


class HomeScreen(Screen):
    pass

class CameraScreen(Screen):
    pass

class AttendanceScreen(Screen):
    
    pass

class AttendanceApp(MDApp):
    df = pandas.read_excel("Book1.xlsx")
    attendance_number = NumericProperty(df.shape[0])
    def option_callback(self , text_of_that_option):
        print(text_of_that_option)
    
    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.material_style = "M3"
        self.theme_cls.accent_palette = 'Red'
        kv = Builder.load_file('attendance.kv')
        return kv
    
    

AttendanceApp().run()

