import json
from jinja2 import Template
import argparse
from pathlib import Path

def main(args):
    filename = Path(args.jsonresume).stem
    output_filename = args.output if args.output is not None else "output.tex"
    
    with open(args.jsonresume) as json_file:
        data = json.load(json_file)
    
    with open(args.template) as tex_template:
        template = Template(tex_template.read(), comment_start_string="<<", comment_end_string=">>")

    output_tex = template.render(data)

    # Sauvegarder le fichier rempli
    with open(output_filename, 'w') as output_file:
        output_file.write(output_tex)

parser = argparse.ArgumentParser(description="Fill Latex resume template with JsonResume")
parser.add_argument("jsonresume", help="JsonResume input")
parser.add_argument("template", help="Latex template")
parser.add_argument('-o', "--output", help="Output filename of the generated tex resume")
args = parser.parse_args()
config = vars(args)
main(args)