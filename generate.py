#!/usr/bin/env python3

import markdown
import os, sys
import json
import re
import shutil
import urllib

COURSES_DIR = 'courses'
HTML_DIR = 'docs'
META_FILE = 'meta.json'
TEMPLATE_FILE = 'template.html'
INDEX_FILE = 'index.html'
REDIRECT_FILE = 'redirect.html'
EXCLUDE_DIR = ['images', 'css', 'scss', 'js', 'download']
COPY_DIR = ['images', 'css', 'js', 'download']
MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']
MARKDOWN_EXTENSIONS_CONFIGS = {
    'codehilite': {
        'guess_lang': False
    }
}

DEBUG = True

def debug_print(text):
    if DEBUG:
        print(text)

def sort_by_num(a):
    def ignore_prefix(e):
        return re.sub('^[0-9]+ *', '', e)
    a.sort(key=ignore_prefix)

    def prefix_int(e):
        prefix = re.match('[0-9]+', e)
        if prefix:
            return int(prefix.group(0))
        return -1
    a.sort(key=prefix_int)

def get_dir(path):
    dirs = []
    entries = os.scandir(path)
    for entry in entries:
        if entry.is_dir() and entry.name[0] != 'd':
            if entry.name not in EXCLUDE_DIR:
                dirs.append(entry.name)
    sort_by_num(dirs)
    return dirs

def get_md_files(path):
    md_files = []
    entries = os.scandir(path)
    for entry in entries:
        if not entry.is_dir() and entry.name[-3:] == '.md' and entry.name[0] != 'd':
            md_files.append(entry.name)
    sort_by_num(md_files)
    return md_files

def get_meta(directory):
    file = os.path.join(directory, META_FILE)
    try:
        f = open(file)
        return json.load(f)
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError as e:
        print('JSON decode error: ' + file)
        print(e)
        sys.exit()

def get_course_meta(directory, course):
    default_meta = {
        'title': course,
        'shortDescription': ''
    }

    meta = get_meta(directory)
    if meta == None:
        file = os.path.join(directory, META_FILE)
        f = open(file, 'w')
        json.dump(default_meta, f, indent=4)
    else:
        default_meta['title'] = get_prop(meta, 'title', course)
        default_meta['shortDescription'] = get_prop(meta, 'shortDescription', '')

    return default_meta

def get_section_meta(directory, section):
    default_meta = {
        'title': section
    }

    meta = get_meta(directory)
    if meta == None:
        file = os.path.join(directory, META_FILE)
        f = open(file, 'w')
        json.dump(default_meta, f, indent=4)
    else:
        default_meta['title'] = get_prop(meta, 'title', section)

    return default_meta

def get_template(directory):
    file = os.path.join(directory, TEMPLATE_FILE)
    try:
        f = open(file)
        return f.read()
    except:
        return None

def get_redirect(directory):
    file = os.path.join(directory, REDIRECT_FILE)
    try:
        f = open(file)
        return f.read()
    except:
        return None

def get_md_content(directory, filename):
    file = os.path.join(directory, filename)
    f = open(file)
    return f.read()

def get_md_title(directory, filename):
    file = os.path.join(directory, filename)
    f = open(file)
    first_line = f.readline()
    if first_line[0:2] == '# ':
        return first_line[2:].strip()
    else:
        return first_line.strip()

def get_prop(meta, prop, default):
    if meta and prop in meta:
        return meta[prop]
    else:
        return default

def gen_toc_html(toc, filename):
    html = ''
    for section in toc:
        html += '<p>' + section['title'] + '</p>'
        html += '<ul>'
        for page in section['pages']:
            if filename == page['path']:
                ele_class = 'class="current"'
            else:
                ele_class = ''
            url = urllib.parse.quote('../' + page['path'])
            html += '<a href="' + url + '"><li ' + ele_class + '>' + page['title'] + '</li></a>'
        html += '</ul>'
    return html

def gen_directory_html(directory):
    html = '<ul>'
    for course in directory:
        url = urllib.parse.quote(directory[course])
        html += '<li><a href="' + url + '">' + course + '</a></li>'
    html += '</ul>'
    return html

def gen_html(template, subs):
    out = template
    for sub in subs:
        out = out.replace('#' + sub + '#', subs[sub])
    return out

def mkdir_if_needed(*args):
    path = ''
    for directory in args:
        path = os.path.join(path, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        elif not os.path.isdir(path):
            print('Path exist, but is not a directory: ' + path)
            sys.exit()
    return path

def write_html(html, course, section, filename):
    path = mkdir_if_needed(HTML_DIR, course, section)
    path = os.path.join(path, filename)
    
    f = open(path, mode='w')
    f.write(html)
    f.close()

def copy_excludes(course):
    for directory in COPY_DIR:
        src = os.path.join(COURSES_DIR, course, directory)
        dest = os.path.join(HTML_DIR, course, directory)
        dest = filter_out_path(dest)
        if os.path.isdir(src):
            print('    ' + directory)
            if os.path.exists(dest):
                shutil.rmtree(dest)
            shutil.copytree(src, dest)

def compile_scss(course):
    src = os.path.join(COURSES_DIR, course, 'scss')
    if not os.path.isdir(src):
        return
    dest = mkdir_if_needed(HTML_DIR, course, 'css')
    
    os.system('sass --sourcemap=none --update ' + src + ':' + dest)

def compile_md(content):
    return markdown.markdown(content, extensions=MARKDOWN_EXTENSIONS, extension_configs=MARKDOWN_EXTENSIONS_CONFIGS)

def filter_out_path(path):
    return re.sub(' ', '-', path)
    
### Main ###

# Clean up
if os.path.isdir(HTML_DIR):
    print('Removing html directory: ' + HTML_DIR)
    shutil.rmtree(HTML_DIR)
elif os.path.exists(HTML_DIR):
    print('html exists but is not directory: ' + HTML_DIR)
    sys.exit()

# Root
print('Processing root')
root_template = get_template(COURSES_DIR)
root_redirect = get_redirect(COURSES_DIR)

print('  Copying directories: ')
copy_excludes('.')

print('  Compile SCSS')
compile_scss('.')

# Courses
courses = get_dir(COURSES_DIR)
print('Courses found: ' + str(courses) + '\n')

directory = {}

for course in courses:
    print('Processing course: ' + course)
    course_path = os.path.join(COURSES_DIR, course)
    course_out = filter_out_path(course)

    course_meta = get_course_meta(course_path, course)
    course_title = course_meta['title']
    course_short_description = course_meta['shortDescription']
    
    course_template = get_template(course_path)
    course_redirect = get_redirect(course_path)

    print('  Copying directories: ')
    copy_excludes(course)

    print('  Compile SCSS')
    compile_scss(course)

    # Generate table of content
    sections = get_dir(course_path)
    toc = []

    for section in sections:
        print('  Section found: ' + section)
        section_path = os.path.join(course_path, section)
        section_out = filter_out_path(section)

        section_meta = get_section_meta(section_path, section)
        section_title = section_meta['title']
        
        pages = get_md_files(section_path)

        toc_section = {
            'title': section_title,
            'pages': []
        }
        
        for page in pages:
            print('    Page: '  + page)
            filename_out = filter_out_path(page[:-3] + '.html')
            
            if not course_title in directory:
                directory[course_title] = urllib.parse.quote(course_out + '/' + section_out + '/' + filename_out)

            page_title = get_md_title(section_path, page)
            toc_section['pages'].append({
                'title': page_title,
                'path': urllib.parse.quote(section_out + '/' + filename_out)
            })

        toc.append(toc_section)

    # Generate pages
    print('Generating pages for course: ' + course)
    course_first_page = None

    for section in sections:
        print('  Section : ' + section)
        section_path = os.path.join(course_path, section)
        section_out = filter_out_path(section)

        section_template = get_template(section_path)
        section_redirect = get_redirect(section_path)
        
        section_meta = get_section_meta(section_path, section)
        section_title = section_meta['title']
        
        pages = get_md_files(section_path)

        section_first_page = None

        for page in pages:
            print('    Page: ' + page)
            filename_out = filter_out_path(page[:-3] + '.html')

            if not course_first_page:
                course_first_page = section_out + '/' + filename_out
            if not section_first_page:
                section_first_page = filename_out

            content = get_md_content(section_path, page)
            content_html = compile_md(content)

            toc_html = gen_toc_html(toc, section_out + '/' + filename_out)

            template = root_template
            if course_template:
                template = course_template
            if section_template:
                template = section_template
                
            html = gen_html(template, {
                'title': course_title,
                'toc': toc_html,
                'content': content_html,
                'courseShortDescription': course_short_description
            })

            write_html(html, course_out, section_out, filename_out)
        
        print('    Generate section redirect page')
        redirect = root_redirect
        if course_redirect:
            redirect = course_redirect
        if section_redirect:
            redirect = section_redirect
        html = gen_html(redirect, {
            'redirectURL': urllib.parse.quote(section_first_page)
        })
        write_html(html, course_out, section_out, 'index.html')

    print('  Generate course redirect page')
    redirect = root_redirect
    if course_redirect:
        redirect = course_redirect
    html = gen_html(redirect, {
        'redirectURL': urllib.parse.quote(course_first_page)
    })
    write_html(html, course_out, '.', 'index.html')

file = os.path.join(COURSES_DIR, INDEX_FILE)
f = open(file)
template =  f.read()
html = gen_html(template, {
    'directory': gen_directory_html(directory)
})

write_html(html, '.', '.', 'index.html')