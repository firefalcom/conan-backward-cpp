from conan import ConanFile
from conan.tools.files import copy
from os.path import join

class BackwardCppConan(ConanFile):
    name = "backward-cpp"
    version = "1.5"
    license = "MIT"
    author = "François-Xavier Bourlet"
    url = "https://github.com/bombela/backward-cpp"
    description = "A beautiful stack trace pretty printer for C++"
    topics = ("stacktrace", "debug")

    def source(self):
        self.run("git clone https://github.com/bombela/backward-cpp")
        self.run("cd backward-cpp && git checkout v%s" % self.version)

    def package(self):
        copy(self, "backward.hpp", join(self.source_folder, "backward-cpp"), join(self.package_folder, "include"))
        copy(self, "backward.cpp", join(self.source_folder, "backward-cpp"), join(self.package_folder, "include"))

    def package_id(self):
        self.info.clear()

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.srcdirs = ['src']
