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
dst_lib_dir = ""
dst_usr_lib_dir = ""
cc_sdk_sysroot = ""

def set_global(args):
    global pkg_path
    global output_dir
    global dst_lib_dir
    global dst_usr_lib_dir
    global arch
    global arch_cc_version
    global cross_compiler_tarball
    global cross_compiler_tarball_type
    global cross_compiler_tarball_root
    global cc_path
    global cc_name
    global cc_sysroot_lib
    global cc_sysroot_usr_lib
    global cc_version
    global cc_sdk_sysroot
    global pkgconfig_dir
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    arch = ops.getEnv("ARCH_ALT")
    pkg_args = args["pkg_args"]
    arch_cc_version = pkg_args["version"]
    if arch_cc_version == "Linaro-2017.01":
        cross_compiler_tarball = ops.path_join(pkg_path, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabi.tar.xz")
        cross_compiler_tarball_type = "XZ"
        cross_compiler_tarball_root = "/opt" #ops.path_join("/opt", "IOPC")
        cc_path=ops.path_join(output_dir, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabi/bin")
        #cc_name=ops.path_join(cc_path, "arm-linux-gnueabi-")
        cc_name="arm-linux-gnueabi-"
        cc_sysroot_lib = ops.path_join(output_dir, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabi/arm-linux-gnueabi/libc/lib")
        cc_sdk_sysroot = ops.path_join(output_dir, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabi/arm-linux-gnueabi/libc")
        cc_version = "2.21"
    elif arch_cc_version == "Linaro-2017.01hf":
        cross_compiler_tarball = ops.path_join(pkg_path, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabihf.tar.xz")
        cross_compiler_tarball_type = "XZ"
        cross_compiler_tarball_root = "/opt" #ops.path_join("/opt", "IOPC")
        cc_path=ops.path_join(output_dir, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabihf/bin")
        #cc_name=ops.path_join(cc_path, "arm-linux-gnueabihf-")
        cc_name="arm-linux-gnueabihf-"
        cc_sysroot_lib = ops.path_join(output_dir, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabi/arm-linux-gnueabi/libc/lib")
        cc_sysroot_usr_lib = ops.path_join(output_dir, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabi/arm-linux-gnueabi/libc/usr/lib")
        cc_sdk_sysroot = ops.path_join(output_dir, "gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabi/arm-linux-gnueabi/libc")
        cc_version = "2.21"
    elif arch_cc_version == "CodeSourcery-2014.05":
        cross_compiler_tarball = ops.path_join(pkg_path, "arm-2014.05-29-arm-none-linux-gnueabi-i686-pc-linux-gnu.tar.bz2")
        cross_compiler_tarball_type = "BZ2"
        cross_compiler_tarball_root = "/opt" #ops.path_join("/opt", "IOPC")
        cc_path=ops.path_join(output_dir, "arm-2014.05/bin")
        #cc_name=ops.path_join(cc_path, "arm-none-linux-gnueabi-")
        cc_name="arm-none-linux-gnueabi-"
        cc_sysroot_lib = ops.path_join(output_dir, "arm-2014.05/arm-none-linux-gnueabi/libc/armv4t/lib")
        cc_sysroot_usr_lib = ops.path_join(output_dir, "arm-2014.05/arm-none-linux-gnueabi/libc/armv4t/usr/lib")
        cc_sdk_sysroot = ops.path_join(output_dir, "arm-2014.05/arm-none-linux-gnueabi/libc/armv4t")
        cc_version = "2.18"
    elif arch_cc_version == "iopc_gcc_armel_2017.02.3":
        cross_compiler_tarball = ops.path_join(pkg_path, "iopc_gcc_armel_2017.02.3.tar.xz")
        cross_compiler_tarball_type = "XZ"
        cross_compiler_tarball_root = "/opt" #ops.path_join("/opt", "IOPC")
        cc_path=ops.path_join(cross_compiler_tarball_root, "iopc_gcc_armel_2017.02.3/usr/bin")
        #cc_name=ops.path_join(cc_path, "arm-iopc-linux-gnueabi-")
        cc_name="arm-iopc-linux-gnueabi-"
        cc_sysroot_lib = ops.path_join(cross_compiler_tarball_root, "iopc_gcc_armel_2017.02.3/usr/arm-iopc-linux-gnueabi/sysroot/lib")
        cc_sysroot_usr_lib = ops.path_join(cross_compiler_tarball_root, "iopc_gcc_armel_2017.02.3/usr/arm-iopc-linux-gnueabi/sysroot/usr/lib")
        cc_sdk_sysroot = ops.path_join(cross_compiler_tarball_root, "iopc_gcc_armel_2017.02.3/usr/arm-iopc-linux-gnueabi/sysroot")
        cc_version = "2.24"
    elif arch_cc_version == "iopc_gcc_x86_64_2017.02.3":
        cross_compiler_tarball = ops.path_join(pkg_path, "iopc_gcc_x86_64_2017.02.3.tar.xz")
        cross_compiler_tarball_type = "XZ"
        cross_compiler_tarball_root = "/opt" #ops.path_join("/opt", "IOPC")
        cc_path=ops.path_join(cross_compiler_tarball_root, "iopc_gcc_x86_64_2017.02.3/usr/bin")
        #cc_name=ops.path_join(cc_path, "x86_64-iopc-linux-gnu-")
        cc_name="x86_64-iopc-linux-gnu-"
        cc_sysroot_lib = ops.path_join(cross_compiler_tarball_root, "iopc_gcc_x86_64_2017.02.3/usr/x86_64-iopc-linux-gnu/sysroot/lib")
        cc_sysroot_usr_lib = ops.path_join(cross_compiler_tarball_root, "iopc_gcc_x86_64_2017.02.3/usr/x86_64-iopc-linux-gnu/sysroot/usr/lib")
        cc_sdk_sysroot = ops.path_join(cross_compiler_tarball_root, "iopc_gcc_x86_64_2017.02.3/usr/x86_64-iopc-linux-gnu/sysroot")
        cc_version = "2.24"
    else:
        sys.exit(1)

    dst_lib_dir = ops.path_join(output_dir, "lib")
    dst_usr_lib_dir = ops.path_join(iopc.getSdkPath(), "usr/lib")
    pkgconfig_dir = ops.path_join(iopc.getSdkPath(), "pkgconfig")

def MAIN_ENV(args):
    set_global(args)

    ops.exportEnv(ops.addEnv("PATH", cc_path))
    ops.exportEnv(ops.setEnv("CROSS_COMPILE", cc_name))
    ops.exportEnv(ops.setEnv("CC_SYSROOT", cc_sdk_sysroot))
    ops.exportEnv(ops.setEnv("PKG_CONFIG_PATH", pkgconfig_dir))
    return False

def copy_cc_libs():
    # Copy libraries from compiler sysroot
    cc_lib_path = cc_sysroot_lib
    cc_usr_lib_path = cc_sysroot_usr_lib
    ops.mkdir(dst_lib_dir)

    if arch == "any":
        return 

    ops.copyto(ops.path_join(cc_lib_path, "libgcc_s.so.1"), dst_lib_dir)
    ops.copyto(ops.path_join(cc_lib_path, "libgcc_s.so"), dst_lib_dir)

    ops.copyto(ops.path_join(cc_lib_path, "ld-{}.so".format(cc_version)), dst_lib_dir)
    if arch == "armhf":
        ops.copyto(ops.path_join(cc_lib_path, "ld-linux-armhf.so.3"), dst_lib_dir)
        ops.ln(dst_lib_dir, "ld-linux-armhf.so.3", "ld-linux-armhf.so")
    elif arch == "armel":
        ops.copyto(ops.path_join(cc_lib_path, "ld-linux.so.3"), dst_lib_dir)
        ops.ln(dst_lib_dir, "ld-linux.so.3", "ld-linux.so")
    elif arch == "x86_64":
        ops.copyto(ops.path_join(cc_lib_path, "ld-linux-x86-64.so.2"), dst_lib_dir)
        ops.ln(dst_lib_dir, "ld-linux-x86-64.so.2", "ld-linux.so")
    else:
        sys.exit(1)

    ops.copyto(ops.path_join(cc_lib_path, "libc-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libc-{}.so".format(cc_version), "libc.so.6")
    ops.ln(dst_lib_dir, "libc-{}.so".format(cc_version), "libc.so")

    ops.copyto(ops.path_join(cc_lib_path, "librt-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "librt-{}.so".format(cc_version), "librt.so.1")
    ops.ln(dst_lib_dir, "librt-{}.so".format(cc_version), "librt.so")

    ops.copyto(ops.path_join(cc_lib_path, "libpthread-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libpthread-{}.so".format(cc_version), "libpthread.so.0")
    ops.ln(dst_lib_dir, "libpthread-{}.so".format(cc_version), "libpthread.so")

    ops.copyto(ops.path_join(cc_lib_path, "libdl-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libdl-{}.so".format(cc_version), "libdl.so.2")
    ops.ln(dst_lib_dir, "libdl-{}.so".format(cc_version), "libdl.so")

    ops.copyto(ops.path_join(cc_lib_path, "libm-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libm-{}.so".format(cc_version), "libm.so.6")
    ops.ln(dst_lib_dir, "libm-{}.so".format(cc_version), "libm.so")

    ops.copyto(ops.path_join(cc_lib_path, "libcrypt-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libcrypt-{}.so".format(cc_version), "libcrypt.so.1")
    ops.ln(dst_lib_dir, "libcrypt-{}.so".format(cc_version), "libcrypt.so")

    ops.copyto(ops.path_join(cc_lib_path, "libnsl-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libnsl-{}.so".format(cc_version), "libnsl.so.1")
    ops.ln(dst_lib_dir, "libnsl-{}.so".format(cc_version), "libnsl.so")

    ops.copyto(ops.path_join(cc_lib_path, "libnss_compat-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libnss_compat-{}.so".format(cc_version), "libnss_compat.so.2")
    ops.ln(dst_lib_dir, "libnss_compat-{}.so".format(cc_version), "libnss_compat.so")

    ops.copyto(ops.path_join(cc_lib_path, "libnss_db-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libnss_db-{}.so".format(cc_version), "libnss_db.so.2")
    ops.ln(dst_lib_dir, "libnss_db-{}.so".format(cc_version), "libnss_db.so")

    ops.copyto(ops.path_join(cc_lib_path, "libnss_dns-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libnss_dns-{}.so".format(cc_version), "libnss_dns.so.2")
    ops.ln(dst_lib_dir, "libnss_dns-{}.so".format(cc_version), "libnss_dns.so")

    ops.copyto(ops.path_join(cc_lib_path, "libnss_files-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libnss_files-{}.so".format(cc_version), "libnss_files.so.2")
    ops.ln(dst_lib_dir, "libnss_files-{}.so".format(cc_version), "libnss_files.so")

    ops.copyto(ops.path_join(cc_lib_path, "libnss_hesiod-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libnss_hesiod-{}.so".format(cc_version), "libnss_hesiod.so.2")
    ops.ln(dst_lib_dir, "libnss_hesiod-{}.so".format(cc_version), "libnss_hesiod.so")

    ops.copyto(ops.path_join(cc_lib_path, "libnss_nis-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libnss_nis-{}.so".format(cc_version), "libnss_nis.so.2")
    ops.ln(dst_lib_dir, "libnss_nis-{}.so".format(cc_version), "libnss_nis.so")

    ops.copyto(ops.path_join(cc_lib_path, "libnss_nisplus-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libnss_nisplus-{}.so".format(cc_version), "libnss_nisplus.so.2")
    ops.ln(dst_lib_dir, "libnss_nisplus-{}.so".format(cc_version), "libnss_nisplus.so")

    ops.copyto(ops.path_join(cc_lib_path, "libresolv-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libresolv-{}.so".format(cc_version), "libresolv.so.2")
    ops.ln(dst_lib_dir, "libresolv-{}.so".format(cc_version), "libresolv.so")

    ops.copyto(ops.path_join(cc_lib_path, "libutil-{}.so".format(cc_version)), dst_lib_dir)
    ops.ln(dst_lib_dir, "libutil-{}.so".format(cc_version), "libutil.so.1")
    ops.ln(dst_lib_dir, "libutil-{}.so".format(cc_version), "libutil.so")

    ops.copyto(ops.path_join(cc_usr_lib_path, "libstdc++.so.6.0.21"), dst_lib_dir)
    ops.ln(dst_lib_dir, "libstdc++.so.6.0.21", "libstdc++.so.6.0")
    ops.ln(dst_lib_dir, "libstdc++.so.6.0.21", "libstdc++.so.6")
    ops.ln(dst_lib_dir, "libstdc++.so.6.0.21", "libstdc++.so")

def copy_sdk_usr_libs():
    ops.mkdir(dst_usr_lib_dir)
    ops.copyto(ops.path_join(cc_sdk_sysroot, "Mcrt1.o"), dst_usr_lib_dir)
    ops.copyto(ops.path_join(cc_sdk_sysroot, "Scrt1.o"), dst_usr_lib_dir)
    ops.copyto(ops.path_join(cc_sdk_sysroot, "crt1.o"), dst_usr_lib_dir)
    ops.copyto(ops.path_join(cc_sdk_sysroot, "crti.o"), dst_usr_lib_dir)
    ops.copyto(ops.path_join(cc_sdk_sysroot, "crtn.o"), dst_usr_lib_dir)
    ops.copyto(ops.path_join(cc_sdk_sysroot, "gcrt1.o"), dst_usr_lib_dir)

def MAIN_EXTRACT(args):
    set_global(args)
    cc_exist = False

    #ops.mkdir(cross_compiler_tarball_root)
    if ops.isExist(ops.path_join(cross_compiler_tarball_root, arch_cc_version)):
        cc_exist = True

    if not cc_exist:
        if cross_compiler_tarball_type == "XZ":
            ops.unTarXzSUDO(cross_compiler_tarball, cross_compiler_tarball_root)
        elif cross_compiler_tarball_type == "BZ2":
            ops.unTarBz2SUDO(cross_compiler_tarball, cross_compiler_tarball_root)
        elif cross_compiler_tarball_type == "GZ":
            ops.unTarGzSUDO(cross_compiler_tarball, cross_compiler_tarball_root)
        else:
            sys.exit(1)
    #else:
    #    copy_cc_libs()
    copy_cc_libs()
    #copy_sdk_usr_libs()
    ops.mkdir(pkgconfig_dir)

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
    iopc.installBin(args["pkg_name"], ops.path_join(dst_lib_dir, "."), "lib")

    return False

def MAIN_SDKENV(args):
    set_global(args)
    cc_sysroot = ops.getEnv("CC_SYSROOT")
    cflags = ""
    cflags += " -I" + ops.path_join(cc_sysroot, 'usr/include')
    cflags += " -I" + ops.path_join(iopc.getSdkPath(), 'usr/include')
    #cflags += " -I" + ops.path_join(iopc.getSdkPath(), 'usr/include/linux_headers')

    libs = ""
    libs += " -L" + ops.path_join(cc_sysroot, 'lib')
    libs += " -L" + ops.path_join(cc_sysroot, 'usr/lib')
    libs += " -L" + ops.path_join(iopc.getSdkPath(), 'lib')
    #libs += " -L" + ops.path_join(iopc.getSdkPath(), 'usr/lib')
    libs += " -lm -ldl -lpthread -lrt"

    iopc.add_includes(cflags)
    iopc.add_libs(libs)

    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)
    return False

def MAIN(args):
    set_global(args)
    print "cross_compiler"
