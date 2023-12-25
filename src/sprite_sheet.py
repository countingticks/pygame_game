import pygame

def load_image(path): 
    image = pygame.image.load(path).convert_alpha()
    return image

def load_sprite_sheet(sprite_sheet):
    sprite_sheet_image = pygame.image.load(sprite_sheet['sheet']['path']).convert_alpha()

    for group_index, group in enumerate(sprite_sheet['sheet']['groups']):
        sprite_sheet[group]['images'] = []

        for frame in range(sprite_sheet[group]['frames']):
            width = sprite_sheet['sheet']['width']
            height = sprite_sheet['sheet']['height']

            image = pygame.Surface((width, height))
            image.blit(sprite_sheet_image, (0, 0), (width * frame, height * group_index, width, height))
            image.set_colorkey((0, 0, 0))
            sprite_sheet[group]['images'].append(image)

    print(f"Loaded '{sprite_sheet['sheet']['path']}'")
