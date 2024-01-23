from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.distutils")

name = "random-quotes-generator"
default_task = "analyze"


@init
def set_properties(project):
    project.set_property("dir_source_main_python", "src")
    project.set_property("dir_source_unittest_python", "tests")
    project.set_property("source_dist_ignore_patterns", ["*.pyc", ".git*", ".idea*", ".DS_Store"])
    project.set_property("verbose", True)
 