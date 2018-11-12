import zipfile
import os
import sys
import fnmatch

def find_file_using_extention(extn, base_dir='.'):
    matches = []
    for root, dirnames, filenames in os.walk(base_dir):
        for filename in fnmatch.filter(filenames, '*.%s' % extn):
            matches.append(os.path.join(root, filename))
            
    return matches

if __name__ == '__main__':
    cwd = os.getcwd()
    file_name = "asg03_%s.zip" % sys.argv[1]
    zip_file = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)
    zip_file.write('adversarialAgents.py')
    
    pdf_files = find_file_using_extention('pdf')
    png_files = find_file_using_extention('png')
    jpg_files = find_file_using_extention('jpg')
    jpeg_files = find_file_using_extention('jpeg')
    
    all_files = pdf_files + png_files + jpg_files + jpeg_files
    for f in all_files:
        zip_file.write(f)

    zip_file.close()
