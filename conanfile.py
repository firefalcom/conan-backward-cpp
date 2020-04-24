from conans import ConanFile, CMake, tools

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
        self.copy("*.hpp", dst="include", src="backward-cpp/" )
        self.copy("*.cpp", dst="src", src="backward-cpp/" )

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.srcdirs = ['src']
