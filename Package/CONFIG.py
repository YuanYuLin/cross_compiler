import ops

def MAIN_ENV(args):
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    cross_compile_tarball = pkg_path + "/gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabihf.tar.xz"
    cc_path=output_dir + "/gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabihf/bin"
    cc_name="arm-linux-gnueabihf-"

    env = ops.addEnv("PATH", cc_path)
    ops.exportEnv(env)
    env = ops.setEnv("CROSS_COMPILE", cc_name)
    ops.exportEnv(env)
    env = ops.setEnv("cross_compiler_tarball", cross_compile_tarball)
    ops.exportEnv(env)
    return False

def MAIN_EXTRACT(args):
    output_dir = args["output_path"]
    cross_compiler_tarball = ops.getEnv("cross_compiler_tarball")
    ops.unTarXz(cross_compiler_tarball, output_dir)
    return True

def MAIN_CONFIGURE(args):
    output_dir = args["output_path"]
    return False

def MAIN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN_INSTALL(args):
    output_dir = args["output_path"]
    return False

def MAIN_CLEAN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN(args):
    print "cross_compile"
