from typing import Optional, TypedDict


class Component(TypedDict):
    name: str
    price: int
    tier: int
    compatibility_key: str | int | None
    spec: str
    reasoning: str


cpus: dict[str, list[Component]] = {
    "Intel": [
        {
            "name": "Intel Core i3-12100F",
            "price": 7000,
            "tier": 1,
            "compatibility_key": "LGA1700",
            "spec": "4 Cores / 8 Threads",
            "reasoning": "Excellent entry-level CPU for budget gaming and general use. Offers great single-core performance for its price.",
        },
        {
            "name": "Intel Core i5-12400F",
            "price": 11000,
            "tier": 1,
            "compatibility_key": "LGA1700",
            "spec": "6 Cores / 12 Threads",
            "reasoning": "A fantastic value-for-money CPU, providing a solid foundation for mid-range gaming and productivity without breaking the bank.",
        },
        {
            "name": "Intel Core i5-13400F",
            "price": 18000,
            "tier": 2,
            "compatibility_key": "LGA1700",
            "spec": "10 Cores / 16 Threads",
            "reasoning": "Great for mid-to-high-end builds, offering a mix of Performance and Efficient cores for multitasking and gaming.",
        },
        {
            "name": "Intel Core i7-13700K",
            "price": 35000,
            "tier": 3,
            "compatibility_key": "LGA1700",
            "spec": "16 Cores / 24 Threads",
            "reasoning": "A powerhouse for high-end gaming and content creation, with high clock speeds and a significant core count for demanding tasks.",
        },
        {
            "name": "Intel Core i9-13900K",
            "price": 55000,
            "tier": 3,
            "compatibility_key": "LGA1700",
            "spec": "24 Cores / 32 Threads",
            "reasoning": "The top-tier choice for professionals needing maximum performance for tasks like video editing, 3D rendering, and heavy computation.",
        },
    ],
    "AMD": [
        {
            "name": "AMD Ryzen 5 5500",
            "price": 8000,
            "tier": 1,
            "compatibility_key": "AM4",
            "spec": "6 Cores / 12 Threads",
            "reasoning": "An affordable 6-core processor on the mature AM4 platform, making it a cost-effective choice for entry-level builds.",
        },
        {
            "name": "AMD Ryzen 5 5600",
            "price": 11500,
            "tier": 1,
            "compatibility_key": "AM4",
            "spec": "6 Cores / 12 Threads",
            "reasoning": "One of the best budget CPUs for gaming, offering strong performance and efficiency on the widely available AM4 platform.",
        },
        {
            "name": "AMD Ryzen 5 7600",
            "price": 19000,
            "tier": 2,
            "compatibility_key": "AM5",
            "spec": "6 Cores / 12 Threads",
            "reasoning": "A modern CPU on the AM5 platform, bringing DDR5 and PCIe 5.0 support for a future-proof mid-range system with excellent gaming performance.",
        },
        {
            "name": "AMD Ryzen 7 7800X3D",
            "price": 34000,
            "tier": 3,
            "compatibility_key": "AM5",
            "spec": "8 Cores / 16 Threads",
            "reasoning": "Arguably the best gaming CPU available, thanks to its massive 3D V-Cache, which significantly boosts frame rates in many titles.",
        },
        {
            "name": "AMD Ryzen 9 7950X",
            "price": 48000,
            "tier": 3,
            "compatibility_key": "AM5",
            "spec": "16 Cores / 32 Threads",
            "reasoning": "The ultimate CPU for productivity on the AM5 platform, delivering exceptional multi-threaded performance for the most demanding applications.",
        },
    ],
}
motherboards: dict[str, list[Component]] = {
    "LGA1700": [
        {
            "name": "MSI PRO H610M-G DDR4",
            "price": 7500,
            "tier": 1,
            "compatibility_key": "DDR4",
            "spec": "H610 Chipset",
            "reasoning": "A no-frills, budget-friendly motherboard that gets the job done for entry-level Intel builds, using affordable DDR4 RAM.",
        },
        {
            "name": "ASRock B760M PG Lightning",
            "price": 12000,
            "tier": 2,
            "compatibility_key": "DDR5",
            "spec": "B760 Chipset",
            "reasoning": "A solid B760 board that supports faster DDR5 memory and offers better features than H610, ideal for mid-range systems.",
        },
        {
            "name": "Gigabyte Z790 AORUS ELITE AX",
            "price": 25000,
            "tier": 3,
            "compatibility_key": "DDR5",
            "spec": "Z790 Chipset",
            "reasoning": "A high-end Z790 motherboard with robust power delivery, Wi-Fi 6E, and overclocking support for enthusiast-grade Intel CPUs.",
        },
    ],
    "AM4": [
        {
            "name": "MSI A520M-A PRO",
            "price": 5000,
            "tier": 1,
            "compatibility_key": "DDR4",
            "spec": "A520 Chipset",
            "reasoning": "The most basic and affordable option for AMD's AM4 platform, perfect for ultra-budget builds where every rupee counts.",
        },
        {
            "name": "ASUS TUF GAMING B550M-PLUS",
            "price": 11000,
            "tier": 2,
            "compatibility_key": "DDR4",
            "spec": "B550 Chipset",
            "reasoning": "A feature-rich B550 board known for its durability and performance, offering PCIe 4.0 support for GPUs and SSDs.",
        },
    ],
    "AM5": [
        {
            "name": "ASRock A620M-HDV/M.2+",
            "price": 9000,
            "tier": 2,
            "compatibility_key": "DDR5",
            "spec": "A620 Chipset",
            "reasoning": "An entry point into the AM5 ecosystem, providing essential features and DDR5 support without the high cost of B650/X670 boards.",
        },
        {
            "name": "Gigabyte B650 GAMING X AX",
            "price": 18000,
            "tier": 3,
            "compatibility_key": "DDR5",
            "spec": "B650 Chipset",
            "reasoning": "A well-rounded B650 motherboard with Wi-Fi, good VRMs, and ample connectivity, making it a great pair for mid-to-high-end Ryzen 7000 CPUs.",
        },
    ],
}
rams: dict[str, list[Component]] = {
    "DDR4": [
        {
            "name": "Corsair Vengeance LPX 8GB 3200MHz",
            "price": 2000,
            "tier": 1,
            "compatibility_key": 8,
            "spec": "8GB DDR4",
            "reasoning": "8GB is the bare minimum for light use and some older games. This kit is affordable and reliable.",
        },
        {
            "name": "G.Skill Ripjaws V 16GB (8GBx2) 3600MHz",
            "price": 4000,
            "tier": 2,
            "compatibility_key": 16,
            "spec": "16GB DDR4",
            "reasoning": "16GB in dual-channel is the sweet spot for modern gaming and multitasking, and this 3600MHz kit is fast and dependable.",
        },
    ],
    "DDR5": [
        {
            "name": "Crucial Pro 16GB (8GBx2) 5600MHz",
            "price": 5500,
            "tier": 2,
            "compatibility_key": 16,
            "spec": "16GB DDR5",
            "reasoning": "A solid 16GB starter kit for DDR5 platforms, offering a good balance of speed and capacity for gaming and general productivity.",
        },
        {
            "name": "G.Skill Trident Z5 Neo 32GB (16GBx2) 6000MHz",
            "price": 11000,
            "tier": 3,
            "compatibility_key": 32,
            "spec": "32GB DDR5",
            "reasoning": "32GB of high-speed DDR5 RAM is ideal for heavy multitasking, content creation, and future-proofing a high-end build. 6000MHz CL30 is the sweet spot for Ryzen 7000.",
        },
    ],
}
gpus: dict[str, list[Component]] = {
    "NVIDIA": [
        {
            "name": "NVIDIA GeForce RTX 3050 8GB",
            "price": 22000,
            "tier": 1,
            "compatibility_key": 450,
            "spec": "8GB GDDR6 VRAM",
            "reasoning": "A decent entry-level GPU for 1080p gaming, capable of running most modern titles at medium settings. Good for budget-conscious gamers.",
        },
        {
            "name": "NVIDIA GeForce RTX 4060 8GB",
            "price": 30000,
            "tier": 2,
            "compatibility_key": 550,
            "spec": "8GB GDDR6 VRAM",
            "reasoning": "The mainstream choice for 1080p gaming, offering excellent performance and power efficiency, plus access to DLSS 3 Frame Generation.",
        },
        {
            "name": "NVIDIA GeForce RTX 4070 Ti SUPER 16GB",
            "price": 85000,
            "tier": 3,
            "compatibility_key": 750,
            "spec": "16GB GDDR6X VRAM",
            "reasoning": "A high-performance GPU perfect for 1440p and even 4K gaming. Its 16GB VRAM is also great for AI/ML and high-resolution video editing.",
        },
    ],
    "AMD": [
        {
            "name": "AMD Radeon RX 6600 8GB",
            "price": 20000,
            "tier": 1,
            "compatibility_key": 500,
            "spec": "8GB GDDR6 VRAM",
            "reasoning": "Often hailed as the king of budget 1080p gaming, the RX 6600 offers unbeatable performance for its price, focusing on raw rasterization power.",
        },
        {
            "name": "AMD Radeon RX 7600",
            "price": 25000,
            "tier": 2,
            "compatibility_key": 550,
            "spec": "8GB GDDR6 VRAM",
            "reasoning": "A strong competitor for 1080p gaming, offering solid performance and modern features on the RDNA 3 architecture.",
        },
        {
            "name": "AMD Radeon RX 7700 XT 12GB",
            "price": 45000,
            "tier": 2,
            "compatibility_key": 650,
            "spec": "12GB GDDR6 VRAM",
            "reasoning": "A great card for 1440p gaming, providing more VRAM than its direct competitors, which helps in texture-heavy games.",
        },
        {
            "name": "AMD Radeon RX 7900 XTX 24GB",
            "price": 95000,
            "tier": 3,
            "compatibility_key": 850,
            "spec": "24GB GDDR6 VRAM",
            "reasoning": "AMD's flagship GPU, offering incredible rasterization performance for 4K gaming and a massive 24GB VRAM buffer for productivity workloads.",
        },
    ],
}
storages: list[Component] = [
    {
        "name": "Crucial P3 500GB NVMe SSD",
        "price": 3000,
        "tier": 1,
        "compatibility_key": 500,
        "spec": "500GB NVMe",
        "reasoning": "A fast NVMe SSD is essential for quick boot times and loading. 500GB is a good starting point for the OS and a few key applications/games.",
    },
    {
        "name": "Western Digital Blue SN580 1TB NVMe SSD",
        "price": 6000,
        "tier": 2,
        "compatibility_key": 1000,
        "spec": "1TB NVMe",
        "reasoning": "1TB is the recommended capacity for most users, providing ample space for the OS, numerous games, and applications without compromising on speed.",
    },
    {
        "name": "Samsung 980 Pro 2TB NVMe SSD",
        "price": 14000,
        "tier": 3,
        "compatibility_key": 2000,
        "spec": "2TB NVMe Gen4",
        "reasoning": "A high-speed 2TB Gen4 drive for enthusiasts and professionals who need rapid access to large files, games, and projects.",
    },
]
psus: list[Component] = [
    {
        "name": "Deepcool PK450D 450W 80+ Bronze",
        "price": 3000,
        "tier": 1,
        "compatibility_key": 450,
        "spec": "450W Bronze",
        "reasoning": "A reliable, budget-friendly power supply with enough wattage for entry-level builds. 80+ Bronze certification ensures decent efficiency.",
    },
    {
        "name": "Cooler Master MWE 550W 80+ Bronze",
        "price": 4000,
        "tier": 1,
        "compatibility_key": 550,
        "spec": "550W Bronze",
        "reasoning": "Provides a comfortable amount of power for entry-level to mid-range GPUs, giving you a bit of headroom for future upgrades.",
    },
    {
        "name": "Corsair CV650 650W 80+ Bronze",
        "price": 5500,
        "tier": 2,
        "compatibility_key": 650,
        "spec": "650W Bronze",
        "reasoning": "A 650W PSU is a safe and solid choice for most mid-range builds, comfortably powering GPUs like the RTX 4060 or RX 7600.",
    },
    {
        "name": "Corsair RM750e 750W 80+ Gold",
        "price": 9000,
        "tier": 2,
        "compatibility_key": 750,
        "spec": "750W Gold Modular",
        "reasoning": "A high-quality, Gold-rated PSU with plenty of power for high-end components. Its modular design helps with clean cable management.",
    },
    {
        "name": "MSI MPG A1000G 1000W 80+ Gold",
        "price": 15000,
        "tier": 3,
        "compatibility_key": 1000,
        "spec": "1000W Gold Modular",
        "reasoning": "For top-tier systems with power-hungry CPUs and GPUs. 1000W ensures stability and provides significant headroom for overclocking and future parts.",
    },
]
cases: list[Component] = [
    {
        "name": "Ant Esports ICE-100",
        "price": 3000,
        "tier": 1,
        "compatibility_key": None,
        "spec": "Mid Tower ATX",
        "reasoning": "A popular budget case that offers good value with pre-installed fans and a mesh front for decent airflow, without a high price tag.",
    },
    {
        "name": "Lian Li Lancool 215",
        "price": 6500,
        "tier": 2,
        "compatibility_key": None,
        "spec": "Mid Tower ATX",
        "reasoning": "Known for its excellent thermal performance thanks to two large front fans, this case provides top-tier airflow for high-performance components.",
    },
    {
        "name": "NZXT H7 Flow",
        "price": 11000,
        "tier": 3,
        "compatibility_key": None,
        "spec": "Mid Tower ATX",
        "reasoning": "A premium case with a clean aesthetic, great airflow, and excellent cable management features, making the building process a pleasure.",
    },
]


def get_budget_tier(budget: int) -> int:
    if budget < 55000:
        return 1
    if budget < 120000:
        return 2
    return 3


def get_use_case_priority(use_cases: list[str]) -> str:
    if not use_cases:
        return "Balanced"
    if "AI/ML" in use_cases:
        return "GPU_Heavy"
    if "Gaming" in use_cases:
        return "GPU_Focused"
    if "Content Creation" in use_cases or "Development" in use_cases:
        return "CPU_Focused"
    return "Balanced"


def _get_component_price(component: Component) -> int:
    return component["price"]


def find_component(
    component_list: list[Component], tier: int, max_price: float
) -> Optional[Component]:
    best_fit = None
    for comp in component_list:
        if comp["tier"] <= tier and comp["price"] <= max_price:
            if best_fit is None or comp["price"] > best_fit["price"]:
                best_fit = comp
    if best_fit is None and component_list:
        return min(component_list, key=_get_component_price)
    return best_fit


def get_recommendation_from_db(
    budget: int, use_cases: list[str], other_reqs: str
) -> Optional[dict[str, Component]]:
    tier = get_budget_tier(budget)
    priority = get_use_case_priority(use_cases)
    allocations = {
        "GPU_Heavy": {
            "CPU": 0.2,
            "GPU": 0.45,
            "RAM": 0.08,
            "MOBO": 0.1,
            "STORAGE": 0.07,
            "PSU": 0.05,
            "CASE": 0.05,
        },
        "GPU_Focused": {
            "CPU": 0.22,
            "GPU": 0.4,
            "RAM": 0.07,
            "MOBO": 0.11,
            "STORAGE": 0.08,
            "PSU": 0.06,
            "CASE": 0.06,
        },
        "CPU_Focused": {
            "CPU": 0.3,
            "GPU": 0.3,
            "RAM": 0.1,
            "MOBO": 0.12,
            "STORAGE": 0.08,
            "PSU": 0.05,
            "CASE": 0.05,
        },
        "Balanced": {
            "CPU": 0.25,
            "GPU": 0.35,
            "RAM": 0.08,
            "MOBO": 0.12,
            "STORAGE": 0.08,
            "PSU": 0.06,
            "CASE": 0.06,
        },
    }[priority]
    build: dict[str, Component] = {}
    pref_cpu = (
        "Intel"
        if "intel" in other_reqs.lower()
        else "AMD"
        if "amd" in other_reqs.lower()
        else None
    )
    pref_gpu = (
        "NVIDIA"
        if "nvidia" in other_reqs.lower()
        else "AMD"
        if "amd" in other_reqs.lower()
        else None
    )
    all_cpus = cpus[pref_cpu] if pref_cpu else cpus["Intel"] + cpus["AMD"]
    selected_cpu = find_component(all_cpus, tier, budget * allocations["CPU"])
    if not selected_cpu:
        return None
    build["CPU"] = selected_cpu
    compatible_mobos = motherboards.get(selected_cpu["compatibility_key"], [])
    selected_mobo = find_component(compatible_mobos, tier, budget * allocations["MOBO"])
    if not selected_mobo:
        return None
    build["Motherboard"] = selected_mobo
    compatible_rams = rams.get(selected_mobo["compatibility_key"], [])
    selected_ram = find_component(compatible_rams, tier, budget * allocations["RAM"])
    if not selected_ram:
        return None
    build["RAM"] = selected_ram
    build["Storage"] = find_component(storages, tier, budget * allocations["STORAGE"])
    build["Case"] = find_component(cases, tier, budget * allocations["CASE"])
    all_gpus = gpus[pref_gpu] if pref_gpu else gpus["NVIDIA"] + gpus["AMD"]
    selected_gpu = find_component(all_gpus, tier, budget * allocations["GPU"])
    if not selected_gpu:
        if "Office Work" in use_cases and tier == 1:
            build["GPU"] = {
                "name": "Integrated Graphics",
                "price": 0,
                "tier": 1,
                "compatibility_key": 150,
                "spec": "Uses CPU's iGPU",
                "reasoning": "For office work and media consumption, the CPU's integrated graphics are sufficient and save a significant amount of budget.",
            }
        else:
            return None
    else:
        build["GPU"] = selected_gpu
    psu_wattage_req = selected_gpu["compatibility_key"] + 100
    compatible_psus = [p for p in psus if p["compatibility_key"] >= psu_wattage_req]
    selected_psu = find_component(compatible_psus, tier, budget * allocations["PSU"])
    if not selected_psu:
        return None
    build["PSU"] = selected_psu
    if any((v is None for v in build.values())):
        return None
    return build