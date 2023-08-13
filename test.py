# from kivymd.app import MDApp
# from kivy.uix.tabbedpanel import TabbedPanel
# from kivy.lang import Builder
# from kivymd.uix.tab.tab import MDTabsBar

# class MainApp(MDApp):
#     def build(self):
#         return MDTabsBar( orientation= 'vertical',)
    
# MainApp().run()

from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCard

KV = '''
<MD3Card>
    padding: 4
    size_hint: None, None
    size: "200dp", "100dp"

    MDRelativeLayout:

        MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"top": 1, "right": 1}

        MDLabel:
            id: label
            text: root.text
            adaptive_size: True
            color: "grey"
            pos: "12dp", "12dp"
            bold: True


MDScreen:

    MDBoxLayout:
        id: box
        adaptive_size: True
        spacing: "56dp"
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class MD3Card(MDCard):
    '''Implements a material design v3 card.'''

    text = StringProperty()


class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def on_start(self):
        styles = {
            "elevated": "#f6eeee", "filled": "#f4dedc", "outlined": "#f8f5f4"
        }
        for style in styles.keys():
            self.root.ids.box.add_widget(
                MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style=style,
                    text=style.capitalize(),
                    md_bg_color=styles[style],
                    shadow_offset=(0, -1),
                )
            )


Example().run()
# from kivymd.app import MDApp
# from kivymd.uix.tab import MDTabsBase
# from kivymd.uix.tab import MDTabs

# class MyTabbedPanel(MDTabs):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.tab_orientation = 'vertical'
        
# class MyTabbedPanelItem(MDTabsBase):
#     pass

# class MyApp(MDApp):
#     def build(self):
#         tp = MyTabbedPanel()
#         tp.add_widget(MyTabbedPanelItem(text='Tab 1'))
#         tp.add_widget(MyTabbedPanelItem(text='Tab 2'))
#         tp.add_widget(MyTabbedPanelItem(text='Tab 3'))
#         return tp

# if __name__ == '__main__':
#     MyApp().run()

# class Test(MDApp):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.screen = MDScreen()
#         menu_items = [
#             {
#                 "viewclass": "OneLineListItem",
#                 "height": dp(56),
#                 "text": f"Item {i}",
#             }
#             for i in range(5)
#         ]
#         self.menu = MDDropdownMenu(items=menu_items, width_mult=4)

#     def open_menu(self, caller):
#         self.menu.caller = caller
#         self.menu.open()

#     def on_start(self):
#         self.screen.add_widget(
#             MDRaisedButton(pos_hint={"center_y": 0.5, "center_x": 0.5}, on_release=self.open_menu)
#         )

#     def build(self):
#         return self.screen

# Test().run()


# from kivymd.app import MDApp
# from kivy.factory import Factory
# from kivy.lang import Builder

# from kivymd.theming import ThemeManager

# Builder.load_string(
#     '''
# #:import toast kivymd.toast.toast


# <MyRoot@BoxLayout>
#     orientation: 'vertical'

#     MDTopAppar:
#         title: "Test MDDropDownItem"
#         md_bg_color: app.theme_cls.primary_color
#         elevation: 10
#         left_action_items: [['menu', lambda x: x]]

#     FloatLayout:

#         MDDropDownItem:
#             id: dropdown_item
#             pos_hint: {'center_x': 0.5, 'center_y': 0.6}
#             items: app.items
#             dropdown_bg: [1, 1, 1, 1]

#         MDRaisedButton:
#             pos_hint: {'center_x': 0.5, 'center_y': 0.3}
#             text: 'Chek Item'
#             on_release: toast(dropdown_item.current_item)
# ''')


# class Test(MDApp):

#     def build(self):
#         self.items = [f"Item {i}" for i in range(50)]
#         return Factory.MyRoot()


# Test().run()

# from kivy.lang import Builder

# from kivymd.app import MDApp
# from kivymd.uix.tab import MDTabsBase
# from kivymd.uix.floatlayout import MDFloatLayout
# from kivymd.icon_definitions import md_icons

# KV = '''
# MDBoxLayout:
#     orientation: "vertical"

#     MDTopAppBar:
#         title: "Example Tabs"

#     MDTabs:
#         id: tabs
#         on_tab_switch: app.on_tab_switch(*args)


# <Tab>

#     MDIconButton:
#         id: icon
#         icon: root.icon
#         icon_size: "48sp"
#         pos_hint: {"center_x": .5, "center_y": .5}
# '''


# class Tab(MDFloatLayout, MDTabsBase):
#     '''Class implementing content for a tab.'''


# class Example(MDApp):
#     icons = list(md_icons.keys())[15:30]

#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Orange"
#         return Builder.load_string(KV)

#     def on_start(self):
#         for tab_name in self.icons:
#             self.root.ids.tabs.add_widget(Tab(icon=tab_name))

#     def on_tab_switch(
#         self, instance_tabs, instance_tab, instance_tab_label, tab_text
#     ):
#         '''
#         Called when switching tabs.

#         :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
#         :param instance_tab: <__main__.Tab object>;
#         :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
#         :param tab_text: text or name icon of tab;
#         '''

#         count_icon = instance_tab.icon  # get the tab icon
#         print(f"Welcome to {count_icon}' tab'")


# Example().run()