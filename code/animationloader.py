import pygame

def load_animation_sets(sheet_path, frame_width, frame_height, rows, cols):
    
    sheet = pygame.image.load(sheet_path).convert_alpha()
    all_animations = []

    for row in range(rows):
        temp_list = []
        for col in range(cols):
            
            x = col * frame_width
            y = row * frame_height
            
            frame = sheet.subsurface((x, y, frame_width, frame_height))
            temp_list.append(frame)
        all_animations.append(temp_list)
        
    return all_animations