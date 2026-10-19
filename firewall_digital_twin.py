"""
Firewall Digital Twin
CYB 301 – Digital Twin Project #2

This program simulates a basic firewall by tracking its state and
responding to commands. It is an educational simulation, not a real firewall.
"""

class Firewall:
    def __init__(self, name, status="OFF", blocked_ips=None, allowed_ips=None, packets_inspected=0):
        self.name = name
        self.status = status
        self.blocked_ips = blocked_ips if blocked_ips is not None else []
        self.allowed_ips = allowed_ips if allowed_ips is not None else []
        self.packets_inspected = packets_inspected

    def start(self):
        """Turn the firewall on."""
        self.status = "ON"
        print(f"{self.name}: Firewall started. Status = {self.status}")

    def stop(self):
        """Turn the firewall off."""
        self.status = "OFF"
        print(f"{self.name}: Firewall stopped. Status = {self.status}")

    def block_ip(self, ip_address):
        """Add an IP address to the blocked list."""
        if ip_address not in self.blocked_ips:
            self.blocked_ips.append(ip_address)
            print(f"{self.name}: Blocked IP address {ip_address}.")
        else:
            print(f"{self.name}: {ip_address} is already blocked.")

    def allow_ip(self, ip_address):
        """Add an IP address to the allowed list."""
        if ip_address not in self.allowed_ips:
            self.allowed_ips.append(ip_address)
            print(f"{self.name}: Allowed IP address {ip_address}.")
        else:
            print(f"{self.name}: {ip_address} is already allowed.")

    def inspect_packet(self, ip_address):
        """Simulate inspecting a packet from an IP address."""
        if self.status != "ON":
            print(f"{self.name}: Cannot inspect traffic because the firewall is OFF.")
            return

        self.packets_inspected += 1
        if ip_address in self.blocked_ips:
            print(f"{self.name}: Packet from {ip_address} BLOCKED.")
        elif ip_address in self.allowed_ips:
            print(f"{self.name}: Packet from {ip_address} ALLOWED.")
        else:
            print(f"{self.name}: Packet from {ip_address} flagged for review (no rule found).")

    def display_status(self):
        """Display the current firewall state."""
        print("\n--- Firewall Status ---")
        print(f"Name: {self.name}")
        print(f"Status: {self.status}")
        print(f"Blocked IPs: {self.blocked_ips}")
        print(f"Allowed IPs: {self.allowed_ips}")
        print(f"Packets inspected: {self.packets_inspected}")
        print("-----------------------\n")


if __name__ == "__main__":
    # Create a digital twin object.
    firewall = Firewall("Campus Firewall")

    # Demonstrate each method and show changes to the object's state.
    firewall.display_status()
    firewall.start()
    firewall.allow_ip("192.168.1.10")
    firewall.block_ip("203.0.113.25")
    firewall.inspect_packet("192.168.1.10")
    firewall.inspect_packet("203.0.113.25")
    firewall.inspect_packet("198.51.100.7")
    firewall.display_status()
    firewall.stop()
    firewall.inspect_packet("192.168.1.10")
