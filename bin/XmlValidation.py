import argparse
from os import listdir
from os.path import isfile, isdir, join

import xmlschema

def validate_against_schema(schema_filename, xml_filename):
    print(f'\nValidating {xml_filename}')
    schema = xmlschema.XMLSchema11(schema_filename)
    if schema.is_valid(xml_filename):
        print(f'Valid XML! ({xml_filename})')
    else:
        schema.validate(xml_filename) # Throws detailed error


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-xml", "--xml", help="Path to the XML file "
                                              "or directory containing .xml or .haml files", required=True, type=str)
    parser.add_argument("-xsd", "--xsd", help="Path to the XSD Schema file", required=True, type=str)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    xml_path = args.xml
    if isfile(xml_path):
        validate_against_schema(schema_filename=args.xsd
                                , xml_filename=xml_path)
    elif isdir(xml_path):
        xml_files = [join(xml_path,filename) for filename in
                     listdir(xml_path)
                     if isfile(join(xml_path,filename))
                     and (filename.endswith('haml')
                          or filename.endswith('xml'))]
        for xml_filename in sorted(xml_files):
            validate_against_schema(schema_filename=args.xsd
                                    , xml_filename=xml_filename)
    else:
        raise Exception(f'I do not know what to do with xml input:{xml_path}')

if __name__ == '__main__':
    main()