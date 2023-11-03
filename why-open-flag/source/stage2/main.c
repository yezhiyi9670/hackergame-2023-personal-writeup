#define _GNU_SOURCE         /* See feature_test_macros(7) */
#include <fcntl.h>
#include <linux/openat2.h>  /* Definition of RESOLVE_* constants */
#include <sys/syscall.h>    /* Definition of SYS_* constants */
#include <unistd.h>

#include <stdio.h>
#include <stdlib.h>

char buf[2048];

int main() {
    // struct file_handle fh;
    // int mount_id = 0;
    
    // name_to_handle_at(AT_FDCWD, "test.txt", &fh, &mount_id, 0);
    // int fd = open_by_handle_at(AT_FDCWD, &fh, 0);
    // printf("%d\n", fd);
    
    // int fd = openat(AT_FDCWD, "test.txt", 0, O_RDONLY);
    
    // int fd = open("test.txt", O_RDONLY);

    struct open_how how = { 0, O_RDONLY };
    int fd = syscall(SYS_openat2, AT_FDCWD, "test.txt", &how, sizeof(how));

    
    read(fd, buf, 2048);
    printf("%s\n", buf);
}
