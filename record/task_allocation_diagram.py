from PIL import Image, ImageDraw, ImageFont
import numpy as np

def draw_illustration_pillow(input_string):
    t_count = ""
    e_count = ""
    
    for i in range(1, len(input_string)):
        if input_string[i].isnumeric():
            t_count += input_string[i]
        else:
            break

    for i in range(len(t_count) + 2, len(input_string)):
        if input_string[i].isnumeric():
            e_count += input_string[i]
        else:
            break

    t_count = int(t_count)
    e_count = int(e_count)

    ms_sequence = input_string.split('_')[1]  # 'm' and 's' sequence
    t_e_mapping = list(map(int, input_string.split('_')[2]))
    e_square_mapping = list(map(int, input_string.split('_')[3].split('-')))
    e_square_mapping = [x + 1 for x in e_square_mapping]

    # Setup image
    img_size = 2000  # Define a larger image size
    img = Image.new('RGB', (img_size, img_size), 'white')
    draw = ImageDraw.Draw(img)

    # Define the size and centers of the squares
    square_size = img_size // 2
    square_centers = [(square_size // 2, square_size // 2),
                      (3 * square_size // 2, square_size // 2),
                      (square_size // 2, 3 * square_size // 2),
                      (3 * square_size // 2, 3 * square_size // 2)]

    # Draw the squares
    counter = 0

    for i, (x_center, y_center) in enumerate(square_centers):
        draw.rectangle([x_center - square_size // 2, y_center - square_size // 2, x_center + square_size // 2, y_center + square_size // 2], outline="black", width=4)
        draw.text((x_center - square_size // 2 + 40, y_center - square_size // 2 + 40), f"C{counter}", fill='black', font=ImageFont.truetype('arial.ttf', 48), anchor='mm')
        counter += 1

    # Calculate 'e' circle positions
    e_positions = {}
    for e_index in range(1, e_count + 1):
        square_index = e_square_mapping[e_index - 1]
        e_center = square_centers[square_index - 1]
        e_positions[e_index] = e_center

    # Adjust 'e' circle positions to avoid overlap
    e_radius = square_size // 8
    for square_index in range(1, 5):
        indices = [i for i, x in enumerate(e_square_mapping, start=1) if x == square_index]
        num_e = len(indices)
        for j, e_index in enumerate(indices, start=1):
            angle = (2 * np.pi / num_e) * (j - 1)
            e_center = square_centers[square_index - 1]
            offset = (3 * e_radius * np.cos(angle), 3 * e_radius * np.sin(angle))
            e_positions[e_index] = (e_center[0] + offset[0], e_center[1] + offset[1])
            draw.ellipse([e_positions[e_index][0] - e_radius, e_positions[e_index][1] - e_radius,
                          e_positions[e_index][0] + e_radius, e_positions[e_index][1] + e_radius],
                         outline='blue', width=4)
            draw.text((e_positions[e_index][0] - 20, e_positions[e_index][1] - 20), f"{ms_sequence[e_index - 1].upper()}", font=ImageFont.truetype('arial.ttf', 48), fill=(0,0,0))

    # Draw 't' circles
    t_radius = e_radius // 5
    for t_index in range(1, t_count + 1):
        e_index = t_e_mapping[t_index - 1]
        e_center = e_positions[e_index]
        num_t = t_e_mapping.count(e_index)
        angle = (2 * np.pi / num_t) * (t_index - 1)
        t_center = (int(e_center[0] + (e_radius - t_radius) * np.cos(angle)),
                    int(e_center[1] + (e_radius - t_radius) * np.sin(angle)))
        draw.ellipse([t_center[0] - t_radius, t_center[1] - t_radius,
                      t_center[0] + t_radius, t_center[1] + t_radius], fill='green', outline='black', width=2)
        # Draw the text at the center of the 't' circle
        draw.text(t_center, str(t_index), fill='white', font=ImageFont.truetype('arial.ttf', 48), anchor='mm')

    # Save the image
    img.save('illustration_fixed.png')
    img.show()

# Example usage
input_string = 't10e7_mmmssss_1122334567_1-1-1-1-1-1-1_655.00KB'
draw_illustration_pillow(input_string)
