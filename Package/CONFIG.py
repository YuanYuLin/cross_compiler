import ops
import iopc

pkg_path = ""
output_dir = ""
arch = ""
arch_cc_version = ""
cross_compiler_tarball = ""
cross_compiler_tarball_type = ""
cross_compiler_tarball_root = ""
cc_path = ""
cc_name = ""
cc_sysroot_lib = ""
cc_version = ""

def set_global(args):
    global pkg_path
    global output_dir
    global arch
    global arch_cc_version
    global cross_compiler_tarball
    global cross_compiler_tarball_type
    global cross_compiler_tarball_root
    global cc_path
    global cc_name
    global cc_sysroot_lib
    global cc_version
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    arch = ops.getEnv("ARCH_ALT")
    pkg_args = args["pkg_args"]
    arch_cc_version = pkg_args["version"]
    if arch == "armhf":
        cross_compiler_tarball = ops.path_join(pkg_path, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabihf.tar.xz")
        cross_compiler_tarball_type = "XZ"
        cross_compiler_tarball_root = output_dir
        cc_path=ops.path_join(output_dir, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabihf/bin")
        cc_name=ops.path_join(cc_path, "arm-linux-gnueabihf-")
        cc_sysroot_lib = ops.path_join(output_dir, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabi/arm-linux-gnueabi/libc/lib")
        cc_version = "2.21"
    elif arch == "armel":
        if arch_cc_version == "Linaro-2017.01":
            cross_compiler_tarball = ops.path_join(pkg_path, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabi.tar.xz")
            cross_compiler_tarball_type = "XZ"
            cross_compiler_tarball_root = output_dir
            cc_path=ops.path_join(output_dir, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabi/bin")
            cc_name=ops.path_join(cc_path, "arm-linux-gnueabi-")
            cc_sysroot_lib = ops.path_join(output_dir, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabi/arm-linux-gnueabi/libc/lib")
            cc_version = "2.21"
        elif arch_cc_version == "CodeSourcery-2014.05":
            cross_compiler_tarball = ops.path_join(pkg_path, "arm-2014.05-29-arm-none-linux-gnueabi-i686-pc-linux-gnu.tar.bz2")
            cross_compiler_tarball_type = "BZ2"
            cross_compiler_tarball_root = output_dir
            cc_path=ops.path_join(output_dir, "arm-2014.05/bin")
            cc_name=ops.path_join(cc_path, "arm-none-linux-gnueabi-")
            cc_sysroot_lib = ops.path_join(output_dir, "arm-2014.05/arm-none-linux-gnueabi/libc/armv4t/lib")
            cc_version = "2.18"
        elif arch_cc_version == "iopc_gcc_armel_2017.02.3":
            cross_compiler_tarball = ops.path_join(pkg_path, "iopc_gcc_armel_2017.02.3.tar.xz")
            cross_compiler_tarball_type = "XZ"
            cross_compiler_tarball_root = "/opt"
            cc_path=ops.path_join(cross_compiler_tarball_root, "iopc_gcc_armel_2017.02.3/usr/bin")
            cc_name=ops.path_join(cc_path, "arm-iopc-linux-gnueabi-")
            cc_sysroot_lib = ops.path_join(cross_compiler_tarball_root, "iopc_gcc_armel_2017.02.3/usr/arm-iopc-linux-gnueabi/sysroot/lib")
            cc_version = "2.24"
        else:
            sys.exit(1)
    else:
        sys.exit(1)

def MAIN_ENV(args):
    set_global(args)

    ops.exportEnv(ops.addEnv("PATH", cc_path))
    ops.exportEnv(ops.setEnv("CROSS_COMPILE", cc_name))
    return False

def MAIN_EXTRACT(args):
    set_global(args)

    if cross_compiler_tarball_root == "/opt":
        if ops.isExist(ops.path_join(cross_compiler_tarball_root, arch_cc_version)):
            return False

    if cross_compiler_tarball_type == "XZ":
        ops.unTarXz(cross_compiler_tarball, cross_compiler_tarball_root)
    elif cross_compiler_tarball_type == "BZ2":
        ops.unTarBz2(cross_compiler_tarball, cross_compiler_tarball_root)
    elif cross_compiler_tarball_type == "GZ":
        ops.unTarGz(cross_compiler_tarball, cross_compiler_tarball_root)
    else:
        sys.exit(1)

    if cross_compiler_tarball_root == "/opt":
        ops.touch(ops.path_join(cross_compiler_tarball_root, arch_cc_version))

    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(output_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)

    return False

def MAIN_BUILD(args):
    set_global(args)

    return False

def MAIN_INSTALL(args):
    set_global(args)
    cc_lib_path = cc_sysroot_lib
 
    if arch == "armhf":
        iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "ld-linux-armhf.so.3"), "lib")

    if arch == "armel":
        iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "ld-linux.so.3"), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libgcc_s.so.1"), "lib")
    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libgcc_s.so"), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "ld-{}.so".format(cc_version)), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libc-{}.so".format(cc_version)), "lib")
    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libc.so.6"), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "librt-{}.so".format(cc_version)), "lib")
    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "librt.so.1"), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libpthread-{}.so".format(cc_version)), "lib")
    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libpthread.so.0"), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libdl-{}.so".format(cc_version)), "lib")
    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libdl.so.2"), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libm-{}.so".format(cc_version)), "lib")
    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libm.so.6"), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libcrypt-{}.so".format(cc_version)), "lib")
    iopc.installBin(args["pkg_name"], ops.path_join(cc_lib_path, "libcrypt.so.1"), "lib")

    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)
    return False

def MAIN(args):
    set_global(args)
    print "cross_compiler"
