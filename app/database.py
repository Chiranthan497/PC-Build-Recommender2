from typing import Optional, TypedDict
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


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
            "name": "Intel Core i5-12600K",
            "price": 16500,
            "tier": 2,
            "compatibility_key": "LGA1700",
            "spec": "10 Cores / 16 Threads",
            "reasoning": "Excellent unlocked CPU for enthusiasts on a budget, offering higher clock speeds and overclocking capability.",
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
            "name": "Intel Core i5-13600K",
            "price": 26000,
            "tier": 2,
            "compatibility_key": "LGA1700",
            "spec": "14 Cores / 20 Threads",
            "reasoning": "A productivity and gaming beast that sits perfectly in the upper mid-range, offering overclocking support and high core counts.",
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
            "name": "AMD Ryzen 3 4100",
            "price": 5500,
            "tier": 1,
            "compatibility_key": "AM4",
            "spec": "4 Cores / 8 Threads",
            "reasoning": "An entry-level quad-core processor sufficient for basic gaming and office tasks on a tight budget.",
        },
        {
            "name": "AMD Ryzen 5 4500",
            "price": 6500,
            "tier": 1,
            "compatibility_key": "AM4",
            "spec": "6 Cores / 12 Threads",
            "reasoning": "An ultra-budget 6-core option that gets you onto the AM4 platform for the lowest possible cost.",
        },
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
            "name": "AMD Ryzen 7 5700X",
            "price": 16000,
            "tier": 2,
            "compatibility_key": "AM4",
            "spec": "8 Cores / 16 Threads",
            "reasoning": "A cost-effective 8-core powerhouse for AM4 users needing more multitasking power without switching platforms.",
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
            "name": "AMD Ryzen 7 7700",
            "price": 28000,
            "tier": 2,
            "compatibility_key": "AM5",
            "spec": "8 Cores / 16 Threads",
            "reasoning": "Excellent efficiency and multi-core performance, making it a great all-rounder for gaming and serious work.",
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
            "name": "ASRock H610M-HVS/M.2",
            "price": 6200,
            "tier": 1,
            "compatibility_key": "DDR4",
            "spec": "H610 Chipset",
            "reasoning": "An ultra-budget friendly H610 board that enables entry into the LGA1700 platform without unnecessary features.",
        },
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
            "name": "Gigabyte A520M K V2",
            "price": 4200,
            "tier": 1,
            "compatibility_key": "DDR4",
            "spec": "A520 Chipset",
            "reasoning": "One of the most affordable AM4 boards available, perfect for maximizing budget towards CPU and GPU.",
        },
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
            "name": "NVIDIA GeForce GTX 1650",
            "price": 12000,
            "tier": 1,
            "compatibility_key": 300,
            "spec": "4GB GDDR6 VRAM",
            "reasoning": "The absolute entry-level dedicated GPU. It can handle eSports titles and older games at 1080p, fitting into tight budgets where integrated graphics aren't enough.",
        },
        {
            "name": "NVIDIA GeForce RTX 3060 12GB",
            "price": 24000,
            "tier": 2,
            "compatibility_key": 550,
            "spec": "12GB GDDR6 VRAM",
            "reasoning": "A workhorse GPU with 12GB VRAM, making it excellent for 1080p gaming and budget-friendly content creation/AI tasks.",
        },
        {
            "name": "NVIDIA GeForce RTX 4060 8GB",
            "price": 29000,
            "tier": 2,
            "compatibility_key": 550,
            "spec": "8GB GDDR6 VRAM",
            "reasoning": "The mainstream choice for 1080p gaming, offering excellent performance and power efficiency, plus access to DLSS 3 Frame Generation.",
        },
        {
            "name": "NVIDIA GeForce RTX 4060 Ti 8GB",
            "price": 36500,
            "tier": 2,
            "compatibility_key": 600,
            "spec": "8GB GDDR6 VRAM",
            "reasoning": "A step up for 1080p high-refresh gaming, offering better rasterization performance than the non-Ti version.",
        },
        {
            "name": "NVIDIA GeForce RTX 4070 SUPER",
            "price": 60000,
            "tier": 3,
            "compatibility_key": 650,
            "spec": "12GB GDDR6X VRAM",
            "reasoning": "A sweet spot for high-refresh 1440p gaming. It offers a significant performance jump and modern features like AV1 encoding.",
        },
        {
            "name": "NVIDIA GeForce RTX 4070 Ti SUPER",
            "price": 82000,
            "tier": 3,
            "compatibility_key": 750,
            "spec": "16GB GDDR6X VRAM",
            "reasoning": "A high-performance GPU perfect for 1440p and entry 4K gaming. Its 16GB VRAM is also great for AI/ML and high-resolution video editing.",
        },
        {
            "name": "NVIDIA GeForce RTX 4080 SUPER",
            "price": 105000,
            "tier": 3,
            "compatibility_key": 750,
            "spec": "16GB GDDR6X VRAM",
            "reasoning": "One of the most powerful GPUs on the market, crushing 4K gaming with ray tracing enabled. A premium choice for enthusiasts.",
        },
    ],
    "AMD": [
        {
            "name": "AMD Radeon RX 6500 XT",
            "price": 14000,
            "tier": 1,
            "compatibility_key": 400,
            "spec": "4GB GDDR6 VRAM",
            "reasoning": "A budget-friendly step up from integrated graphics, suitable for 1080p gaming at medium settings in popular titles.",
        },
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
            "price": 26000,
            "tier": 2,
            "compatibility_key": 550,
            "spec": "8GB GDDR6 VRAM",
            "reasoning": "A strong competitor for 1080p gaming, offering solid performance and modern features on the RDNA 3 architecture.",
        },
        {
            "name": "AMD Radeon RX 6750 XT 12GB",
            "price": 33000,
            "tier": 2,
            "compatibility_key": 650,
            "spec": "12GB GDDR6 VRAM",
            "reasoning": "An excellent value 1440p card with 12GB VRAM, often outperforming newer cards in pure rasterization at this price point.",
        },
        {
            "name": "AMD Radeon RX 7700 XT 12GB",
            "price": 42000,
            "tier": 2,
            "compatibility_key": 650,
            "spec": "12GB GDDR6 VRAM",
            "reasoning": "A great card for 1440p gaming, providing more VRAM than its direct competitors, which helps in texture-heavy games.",
        },
        {
            "name": "AMD Radeon RX 7800 XT 16GB",
            "price": 52000,
            "tier": 3,
            "compatibility_key": 700,
            "spec": "16GB GDDR6 VRAM",
            "reasoning": "A powerhouse for 1440p gaming with a massive 16GB VRAM buffer, offering excellent longevity and value in the high-end segment.",
        },
        {
            "name": "AMD Radeon RX 7900 XT 20GB",
            "price": 74000,
            "tier": 3,
            "compatibility_key": 750,
            "spec": "20GB GDDR6 VRAM",
            "reasoning": "A high-end 4K capable card with 20GB VRAM, bridging the gap between the 7800 XT and the flagship XTX.",
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
    {
        "name": "WD Black SN850X 4TB NVMe SSD",
        "price": 32000,
        "tier": 3,
        "compatibility_key": 4000,
        "spec": "4TB NVMe Gen4",
        "reasoning": "Massive, ultra-fast storage for creative professionals or gamers with huge libraries. No need to uninstall anything ever again.",
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
        "name": "Deepcool PM850D 850W 80+ Gold",
        "price": 10500,
        "tier": 3,
        "compatibility_key": 850,
        "spec": "850W Gold",
        "reasoning": "A sweet spot for high-end builds, capable of powering an RTX 4080 or RX 7900 XTX comfortably with good efficiency.",
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
        "name": "Zebronics Zeb-Cronus",
        "price": 2200,
        "tier": 1,
        "compatibility_key": None,
        "spec": "Mid Tower",
        "reasoning": "A basic functional cabinet that gets the job done for ultra-strict budgets.",
    },
    {
        "name": "Ant Esports ICE-100",
        "price": 3000,
        "tier": 1,
        "compatibility_key": None,
        "spec": "Mid Tower ATX",
        "reasoning": "A popular budget case that offers good value with pre-installed fans and a mesh front for decent airflow, without a high price tag.",
    },
    {
        "name": "Deepcool CC560",
        "price": 4500,
        "tier": 1,
        "compatibility_key": None,
        "spec": "Mid Tower ATX",
        "reasoning": "Offers excellent value with 4 pre-installed LED fans and great airflow, fitting larger components easily.",
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
        "name": "Corsair 4000D Airflow",
        "price": 7000,
        "tier": 2,
        "compatibility_key": None,
        "spec": "Mid Tower ATX",
        "reasoning": "A favorite among builders for its clean design, ease of building, and superb airflow capabilities.",
    },
    {
        "name": "NZXT H7 Flow",
        "price": 11000,
        "tier": 3,
        "compatibility_key": None,
        "spec": "Mid Tower ATX",
        "reasoning": "A premium case with a clean aesthetic, great airflow, and excellent cable management features, making the building process a pleasure.",
    },
    {
        "name": "Lian Li O11 Dynamic Evo",
        "price": 14000,
        "tier": 3,
        "compatibility_key": None,
        "spec": "Mid Tower Dual Chamber",
        "reasoning": "The gold standard for showcase builds. Requires separate fans but offers unmatched aesthetics and liquid cooling support.",
    },
]


def get_budget_tier(budget: int) -> int:
    if budget < 50000:
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
    component_list: list[Component],
    tier: int,
    max_price: float,
    flexibility: float = 1.15,
    component_type: str = "Component",
) -> Optional[Component]:
    logger.info(f"Finding {component_type}: Budget=₹{max_price:,.2f}, Max Tier={tier}")
    suitable_components = [c for c in component_list if c["tier"] <= tier]
    if not suitable_components:
        logger.warning(f"  FAIL: No suitable {component_type} found for tier <= {tier}")
        return None
    valid_components = [c for c in suitable_components if c["price"] <= max_price]
    if valid_components:
        selected = max(valid_components, key=_get_component_price)
        logger.info(f"  SUCCESS: Selected {selected['name']} (₹{selected['price']:,})")
        return selected
    cheapest = min(suitable_components, key=_get_component_price)
    if cheapest["price"] <= max_price * flexibility:
        logger.info(
            f"  FLEXIBLE: Selected {cheapest['name']} (₹{cheapest['price']:,}) - Over budget but within {flexibility}x flexibility"
        )
        return cheapest
    logger.warning(
        f"  FAIL: Cheapest {component_type} ({cheapest['name']} @ ₹{cheapest['price']:,}) exceeds budget limit ₹{max_price * flexibility:,.2f}"
    )
    return None


def get_recommendation_from_db(
    budget: int, use_cases: list[str], other_reqs: str
) -> Optional[dict[str, Component]]:
    if budget < 40000:
        logger.warning(f"Budget ₹{budget:,} is below minimum ₹40,000")
        return None
    logger.info(
        f"--- Starting Build Generation: Budget=₹{budget:,}, Tier={get_budget_tier(budget)} ---"
    )
    tier = get_budget_tier(budget)
    priority = get_use_case_priority(use_cases)
    min_costs = {
        "CPU": 5500,
        "GPU": 12000,
        "RAM": 2000,
        "MOBO": 4200,
        "STORAGE": 3000,
        "PSU": 3000,
        "CASE": 2200,
    }
    total_min_cost = sum(min_costs.values())
    skip_gpu_calc = (
        "Office Work" in use_cases and tier == 1 and ("Gaming" not in use_cases)
    )
    if skip_gpu_calc:
        total_min_cost -= min_costs["GPU"]
    surplus = max(0, budget - total_min_cost)
    logger.info(f"Min Cost: ₹{total_min_cost:,}, Surplus: ₹{surplus:,}")
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
    flexibility = 1.25 if tier == 1 else 1.1
    comp_budgets = {}
    for key, weight in allocations.items():
        base = 0 if key == "GPU" and skip_gpu_calc else min_costs.get(key, 0)
        comp_budgets[key] = base + surplus * weight
        logger.debug(f"Allocated {key}: ₹{comp_budgets[key]:,.2f}")
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
    selected_cpu = find_component(
        all_cpus, tier, comp_budgets["CPU"], flexibility, "CPU"
    )
    if not selected_cpu:
        logger.error("Failed to select CPU")
        return None
    build["CPU"] = selected_cpu
    compatible_mobos = motherboards.get(selected_cpu["compatibility_key"], [])
    selected_mobo = find_component(
        compatible_mobos, tier, comp_budgets["MOBO"], flexibility, "Motherboard"
    )
    if not selected_mobo:
        logger.error(
            f"Failed to select Motherboard for socket {selected_cpu['compatibility_key']}"
        )
        return None
    build["Motherboard"] = selected_mobo
    compatible_rams = rams.get(selected_mobo["compatibility_key"], [])
    selected_ram = find_component(
        compatible_rams, tier, comp_budgets["RAM"], flexibility, "RAM"
    )
    if not selected_ram:
        logger.error(
            f"Failed to select RAM for type {selected_mobo['compatibility_key']}"
        )
        return None
    build["RAM"] = selected_ram
    build["Storage"] = find_component(
        storages, tier, comp_budgets["STORAGE"], flexibility, "Storage"
    )
    if not build["Storage"]:
        logger.error("Failed to select Storage")
        return None
    build["Case"] = find_component(
        cases, tier, comp_budgets["CASE"], flexibility, "Case"
    )
    if not build["Case"]:
        logger.error("Failed to select Case")
        return None
    all_gpus = gpus[pref_gpu] if pref_gpu else gpus["NVIDIA"] + gpus["AMD"]
    selected_gpu = find_component(
        all_gpus, tier, comp_budgets["GPU"], flexibility, "GPU"
    )
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
            logger.info("Using Integrated Graphics for Office build")
        else:
            logger.error("Failed to select GPU")
            return None
    else:
        build["GPU"] = selected_gpu
    base_psu_req = build["GPU"]["compatibility_key"]
    cpu_tier = build.get("CPU", {}).get("tier", 1)
    psu_buffer = 50 if cpu_tier == 3 else 0
    psu_wattage_req = base_psu_req + psu_buffer
    compatible_psus = [p for p in psus if p["compatibility_key"] >= psu_wattage_req]
    current_spend = sum((c["price"] for c in build.values()))
    remaining_budget = budget - current_spend
    if compatible_psus:
        cheapest_suitable_psu = min(compatible_psus, key=_get_component_price)
        current_psu_limit = comp_budgets["PSU"] * flexibility
        if cheapest_suitable_psu["price"] > current_psu_limit:
            if cheapest_suitable_psu["price"] <= remaining_budget:
                logger.info(
                    f"Reallocating budget for PSU: Needed ₹{cheapest_suitable_psu['price']:,}, Available from surplus ₹{remaining_budget:,}"
                )
                comp_budgets["PSU"] = float(cheapest_suitable_psu["price"])
            else:
                logger.warning(
                    f"PSU Reallocation failed: Needed ₹{cheapest_suitable_psu['price']:,}, but only ₹{remaining_budget:,} remaining."
                )
    selected_psu = find_component(
        compatible_psus, tier, comp_budgets["PSU"], flexibility, "PSU"
    )
    if not selected_psu and psu_buffer > 0:
        logger.info("Retrying PSU selection without wattage buffer")
        psu_wattage_req = base_psu_req
        compatible_psus = [p for p in psus if p["compatibility_key"] >= psu_wattage_req]
        selected_psu = find_component(
            compatible_psus, tier, comp_budgets["PSU"], flexibility, "PSU"
        )
    if not selected_psu:
        logger.error(f"Failed to select PSU (Req: {psu_wattage_req}W)")
        return None
    build["PSU"] = selected_psu
    build = optimize_build(build, budget, priority, pref_cpu, pref_gpu)
    logger.info("Build generation successful!")
    return build


def optimize_build(
    build: dict[str, Component],
    total_budget: int,
    priority: str,
    pref_cpu: Optional[str],
    pref_gpu: Optional[str],
) -> dict[str, Component]:
    """
    Iteratively attempts to upgrade components to maximize budget utilization.
    """
    logger.info("--- Starting Build Optimization Phase ---")
    if priority == "GPU_Heavy" or priority == "GPU_Focused":
        upgrade_order = ["GPU", "CPU", "RAM", "Storage", "Motherboard"]
    elif priority == "CPU_Focused":
        upgrade_order = ["CPU", "RAM", "GPU", "Storage", "Motherboard"]
    else:
        upgrade_order = ["GPU", "CPU", "RAM", "Storage"]
    max_iterations = 5
    for _ in range(max_iterations):
        current_cost = sum((c["price"] for c in build.values()))
        remaining = total_budget - current_cost
        if remaining < 500 or remaining < total_budget * 0.01:
            break
        upgraded_any = False
        for comp_type in upgrade_order:
            if comp_type not in build:
                continue
            current_comp = build[comp_type]
            candidates = []
            if comp_type == "GPU":
                if current_comp["name"] == "Integrated Graphics":
                    continue
                gpu_list = gpus[pref_gpu] if pref_gpu else gpus["NVIDIA"] + gpus["AMD"]
                candidates = [c for c in gpu_list if c["price"] > current_comp["price"]]
            elif comp_type == "CPU":
                cpu_list = (
                    cpus["Intel"] if "Intel" in current_comp["name"] else cpus["AMD"]
                )
                candidates = [
                    c
                    for c in cpu_list
                    if c["price"] > current_comp["price"]
                    and c["compatibility_key"] == current_comp["compatibility_key"]
                ]
            elif comp_type == "RAM":
                ddr_type = "DDR5" if "DDR5" in current_comp["spec"] else "DDR4"
                ram_list = rams.get(ddr_type, [])
                candidates = [c for c in ram_list if c["price"] > current_comp["price"]]
            elif comp_type == "Storage":
                candidates = [c for c in storages if c["price"] > current_comp["price"]]
            elif comp_type == "Motherboard":
                mobo_list = motherboards.get(current_comp["spec"].split()[0], [])
                cpu_socket = build["CPU"]["compatibility_key"]
                mobo_list = motherboards.get(cpu_socket, [])
                candidates = [
                    c for c in mobo_list if c["price"] > current_comp["price"]
                ]
            valid_upgrades = [
                c for c in candidates if c["price"] <= current_comp["price"] + remaining
            ]
            if valid_upgrades:
                best_upgrade = max(valid_upgrades, key=_get_component_price)
                cost_increase = best_upgrade["price"] - current_comp["price"]
                if comp_type == "GPU":
                    psu_req = best_upgrade["compatibility_key"]
                    current_psu_wattage = build["PSU"]["compatibility_key"]
                    cpu_tier = build["CPU"]["tier"]
                    needed_wattage = psu_req + (50 if cpu_tier == 3 else 0)
                    if needed_wattage > current_psu_wattage:
                        psu_candidates = [
                            p for p in psus if p["compatibility_key"] >= needed_wattage
                        ]
                        if not psu_candidates:
                            continue
                        cheapest_sufficient_psu = min(
                            psu_candidates, key=_get_component_price
                        )
                        current_psu_price = build["PSU"]["price"]
                        psu_cost_increase = (
                            cheapest_sufficient_psu["price"] - current_psu_price
                        )
                        total_upgrade_cost = cost_increase + psu_cost_increase
                        if total_upgrade_cost <= remaining:
                            logger.info(
                                f"  UPGRADE: GPU to {best_upgrade['name']} + PSU to {cheapest_sufficient_psu['name']} (+₹{total_upgrade_cost:,})"
                            )
                            build["GPU"] = best_upgrade
                            build["PSU"] = cheapest_sufficient_psu
                            remaining -= total_upgrade_cost
                            upgraded_any = True
                            continue
                        else:
                            continue
                logger.info(
                    f"  UPGRADE: {comp_type} from {current_comp['name']} to {best_upgrade['name']} (+₹{cost_increase:,})"
                )
                build[comp_type] = best_upgrade
                remaining -= cost_increase
                upgraded_any = True
        if not upgraded_any:
            break
    final_cost = sum((c["price"] for c in build.values()))
    logger.info(
        f"Optimization Complete. Final Cost: ₹{final_cost:,} ({final_cost / total_budget * 100:.1f}% utilization)"
    )
    return build