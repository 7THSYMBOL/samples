#this script parses the MD file for each sample (which was on the  documentation page)
#and generates a Readme.md file for each sample based on the header comments in the
import os

def generate_readme_md():
    md_dir = "/Users/natashad/Documents/dev/git/streamsx.documentation-gh-pages/samples/spl-for-beginner"
    #for each md_File
    github_list=  open(md_dir + "/file_list")
    md_file_list = github_list.readlines()
    with open("/Users/natashad/Documents/dev/git/samples/Examples-for-beginners/Sample_List") as sample_list_file :
        sample_list = sample_list_file.readlines()
        for sample_name in sample_list:
            sample_name=sample_name.strip()
            #get the sample name
            #see how many .md files start with that sample name, that tells us how many spl files are in the sample.
            sample_source_files = [spl_file.strip() for spl_file in md_file_list if spl_file.startswith(sample_name)]
            with open("/Users/natashad/Documents/dev/git/samples/Examples-for-beginners/" + sample_name + "/README.md", "w") as readme:
                skip_line_break = True #some samples have multiple spl files, show them all in the readme with a line_Break
                for md_file in sample_source_files:#get the list of md files for each sample
                    if len(sample_source_files) > 1:
                        if skip_line_break is False:
                            readme.write("\n---\n")
                        if skip_line_break is True:
                            skip_line_break = False
                    found_delimiter = False
                    with open(md_dir + "/" + md_file) as source:
                        for line in source.readlines():
                            if found_delimiter is True:
                                readme.write(line)
                            if line.startswith("~~~~"):
                                if (found_delimiter is False): readme.write(line)
                                found_delimiter = not(found_delimiter)

    github_list.close()

if __name__ == '__main__':
    generate_readme_md()
