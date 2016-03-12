#!/usr/bin/env python
import os

def setup_items(Group, Item):
    group1 = Group.objects.create(username='langestrst01', selected=False)
    group2 = Group.objects.create(username='ruser', selected=False)

    Item.objects.create(itemid="id_shinyapp1", name="Hello App", dirname="hello", group=group1)
    Item.objects.create(itemid="id_shinyapp2", name="Movie Explorer", dirname="movie_explorer", group=group1)
    Item.objects.create(itemid="id_shinyapp1", name="Hello App", dirname="hello", group=group2)

def save_selected_group(Group,selected_username,selected_status=True):
    found = False
    for group in Group.objects.all():
        if group.username == selected_username:
            group.selected = selected_status
            group.save()
            found = True
    if selected_status == True and found == True:
        for group in Group.objects.all():
            if group.username != selected_username:
                group.selected = False
                group.save()

def get_selected_item(Item,Group):
    selected_group = ''
    for group in Group.objects.all():
        if group.selected:
            selected_group = group.username
    for item in Item.objects.all():
        if item.group.username == selected_group:
            return item
    return Item.first()

if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "innovation.settings")

    from shinyapps.models import ShinyGroup, ShinyItem
    #from fabric.api import run

    setup_items(ShinyGroup, ShinyItem)
    #a = read_item_data(Item)
