import ops

def EXPORT_ENV(args):
    pkg_path=args["pkg_path"]
    cc_path=pkg_path + "/gcc-linaro-5.4.1-2017.01-x86_64_arm-linux-gnueabihf/bin"
    cc_name="arm-linux-gnueabihf-"

    env = {"PATH":cc_path, "CROSS_COMPILE":cc_name}
    return env

def MAIN(args):
    output_path=ops.pkg_mkdir(args["pkg_path"], "debian_jessie_armhf")
    qemu_path=ops.pkg_mkdir(output_path, "/usr/bin")
    print qemu_path
    ops.copyto("/usr/bin/qemu-arm-static", output_path + "/usr/bin/qemu-arm-static")
    arch="armhf"
    CMD=["debootstrap", "--arch=" + arch, "--variant=minbase", "jessie", output_path]
    res = ops.execCmd(CMD, output_path, False, None)
