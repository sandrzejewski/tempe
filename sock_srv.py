# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import socket
import sys
import twisted


TCP_ADDRESS = "127.0.0.1"
TCP_PORT = 10000
TIMEOUT = 60


def main(argv):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((TCP_ADDRESS, TCP_PORT))
    sock.listen(100)
    conn, addr = sock.accept()
    print("Connection:", addr[0], addr[1])
    # data = conn.recv(4096)
    sock.close()


if __name__ == "__main__":
    main(sys.argv)
