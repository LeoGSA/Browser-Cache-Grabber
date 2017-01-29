    # matrix legend: [element in folder_list, header marker, subfolder for to_folder, extention]
full_matrix = [

    ['/jpg', r'ffd8ff', '/jpg/', '.jpg'],                               # JPG
    ['/gif_87', r'4749463837', '/gif_87/', '.gif'],                     # '4749463837' = GIF87
    ['/gif_89', r'4749463839', '/gif_89/', '.gif'],                     # '4749463839' = GIF89
    ['/png', r'89504e47', '/png/', '.png'],                             # '89504e47' = PNG
    ['/video', r'000000206674797069736f6d', '/video/', '.mp4'],         # ....ftypisom = MP4
    ['/video', r'464c56', '/video/', '.flv'],                           # '464c56' = FLV
    ['/video', r'52494646........415649', '/video/', '.avi'],           # '52494646........415649' = RIFF    AVI
    ['/music', r'494433', '/music/', '.mp3'],                           # '494433' = ID3
    ['/html', r'3c21646f63747970652068746d6c', '/html/', '.html'],      # !doctype html
    ['/html', r'3c21444f43545950452068746d6c', '/html/', '.html'],      # !DOCTYPE html
    ['/doc', r'd0cf11e0a1b11ae1', '/doc/', '.doc'],                     # DOC or XLS or PPT
    ['/pdf', r'25504446', '/pdf/', '.pdf'],                             # '25504446' = %PDF
    ['/zip', r'504b0304', '/zip/', '.zip'],                             # ZIP or DOCX or ...
    ['/video', r'474000', '/video/', '.ts'],                            # TS - video file
    ['/ico', r'00000100', '/ico/', '.ico'],                             # ICO
]


