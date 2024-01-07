import pygame

def load_image(sprite): 
    image = pygame.image.load(sprite['path']).convert_alpha()
    sprite['image'] = image

def load_sprite_sheet(sprite_sheet):
    sprite_sheet_image = pygame.image.load(sprite_sheet['sheet']['path']).convert_alpha()
    total_width = 0
    total_height = 0

    for group_index, group in enumerate(sprite_sheet['sheet']['groups']):
        sprite_sheet[group]['images'] = []

        for frame in range(sprite_sheet[group]['frames']):
            if 'width' in sprite_sheet['sheet'] and 'height' in sprite_sheet['sheet']:
                width = sprite_sheet['sheet']['width']
                height = sprite_sheet['sheet']['height']

                image = pygame.Surface((width, height))
                image.blit(sprite_sheet_image, (0, 0), (width * frame, height * group_index, width, height))
                image.set_colorkey((0, 0, 0))
                sprite_sheet[group]['images'].append(image)
            else:
                width = sprite_sheet[group]['width']
                height = sprite_sheet[group]['height']

                image = pygame.Surface((width, height))
                image.blit(sprite_sheet_image, (0, 0), (total_width, total_height, width, height))
                image.set_colorkey((0, 0, 0))
                sprite_sheet[group]['images'].append(image)

                total_width += width

        if not 'width' in sprite_sheet['sheet'] and not 'height' in sprite_sheet['sheet']:
            total_height += sprite_sheet[group]['height']
            total_width = 0

    print(f"Loaded '{sprite_sheet['sheet']['path']}'")


def load_sprite_sheet_test(sprite_sheet):
    for group in sprite_sheet['groups']:
        sprite_sheet[group]['sprite_sheet'] = pygame.image.load(sprite_sheet[group]['path']).convert_alpha()
        total_height = 0

        for _ in range(sprite_sheet[group]['variants']):
            width = sprite_sheet[group]['dimensions'][0]
            height = sprite_sheet[group]['dimensions'][1]

            image = pygame.Surface((width, height))
            image.blit(sprite_sheet[group]['sprite_sheet'], (0, 0), (0, total_height, width, height))
            image.set_colorkey((0, 0, 0))
            sprite_sheet[group]['images'].append(image)

            total_height += height

        print(f"Loaded '{sprite_sheet[group]['path']}'")
