"""
Personalization Service Module

This module provides functionality to adapt content based on user background
without creating duplicate content files. It uses metadata-based filtering
to show relevant examples and explanations based on the user's software or
hardware background.
"""

from typing import Dict, List, Optional, Any
from enum import Enum
from pydantic import BaseModel
import re


class BackgroundType(str, Enum):
    SOFTWARE = "software"
    HARDWARE = "hardware"
    BOTH = "both"


class PersonalizationFilter(BaseModel):
    """Defines what content to show based on user background"""
    software_elements: List[str] = []
    hardware_elements: List[str] = []
    neutral_elements: List[str] = []


class PersonalizationService:
    """
    Service to adapt content based on user background without duplicating files.
    
    The service analyzes content for software/hardware-specific elements
    and filters them based on the user's background.
    """
    
    def __init__(self):
        # Patterns to identify software-specific content
        self.software_patterns = [
            r"\b(software|algorithm|code|programming|script|API|library|framework|SDK|IDE|compiler|debugger|version control|git|repository|branch|merge|pull request|CI/CD|deployment|container|Docker|Kubernetes|virtual environment|package manager|dependency|build system|unit test|integration test|mock|stub|TDD|BDD|refactoring|linting|formatter|profiler|monitoring|logging|tracing|observability|performance|optimization|scalability|reliability|availability|fault tolerance|security|authentication|authorization|encryption|decryption|hash|signature|certificate|protocol|network|HTTP|HTTPS|REST|GraphQL|WebSocket|database|SQL|NoSQL|ORM|migration|seed|backup|restore|cache|session|cookie|middleware|pipeline|workflow|scheduler|queue|message broker|event|pubsub|streaming|batch processing|ETL|data warehouse|ML|AI|model|training|inference|prediction|classification|regression|clustering|neural network|deep learning|tensor|gradient|backpropagation|framework|PyTorch|TensorFlow|scikit-learn|pandas|numpy|matplotlib|seaborn|Jupyter|notebook|environment|configuration|settings|variables|environment variables|config file|YAML|JSON|XML|CSV|parsing|serialization|deserialization|validation|schema|type hint|annotation|decorator|generator|iterator|context manager|async|await|coroutine|thread|process|multiprocessing|multithreading|concurrency|parallelism|synchronization|lock|mutex|semaphore|atomic|race condition|deadlock|starvation|memory management|garbage collection|memory leak|buffer overflow|pointer|reference|dereference|address|allocation|deallocation|heap|stack|static|dynamic|runtime|compile time|interpreter|bytecode|machine code|assembly|binary|executable|library|static library|dynamic library|shared library|object file|linker|loader|symbol|relocation|virtual memory|paging|segmentation|protection|privilege|kernel|user space|system call|interrupt|exception|trap|signal|process|thread|scheduler)\b",
            r"\b(function|method|class|object|inheritance|polymorphism|encapsulation|abstraction|interface|abstract class|constructor|destructor|variable|constant|data type|primitive|composite|array|list|dictionary|hash map|linked list|tree|graph|stack|queue|algorithm|sorting|searching|complexity|Big O|time complexity|space complexity|recursion|iteration|loop|condition|if statement|else|elif|switch|case|for loop|while loop|do while|break|continue|exception handling|try|catch|finally|throw|raise|error|bug|debug|traceback|stack trace|IDE|editor|vim|emacs|sublime|vscode|atom|pycharm|intellij|eclipse|compiler|interpreter|runtime|virtual machine|JVM|CLR|bytecode|assembly|machine code|binary|executable|library|package|module|import|export|require|include|namespace|scope|global|local|closure|higher-order function|lambda|anonymous function|map|filter|reduce|functional programming|object-oriented programming|procedural programming|imperative programming|declarative programming|paradigm|design pattern|MVC|MVVM|singleton|factory|observer|strategy|decorator|adapter|facade|builder|prototype|template method|command|iterator|composite|bridge|flyweight|proxy|chain of responsibility|visitor|mediator|memento|interpreter|state|strategy|template|factory|abstract factory|builder|prototype|adapter|bridge|composite|decorator|facade|flyweight|proxy|chain of responsibility|command|interpreter|iterator|mediator|memento|observer|state|strategy|template|visitor)\b"
        ]
        
        # Patterns to identify hardware-specific content
        self.hardware_patterns = [
            r"\b(hardware|circuit|board|PCB|schematic|component|resistor|capacitor|inductor|diode|transistor|op-amp|microcontroller|MCU|microprocessor|CPU|GPU|FPGA|ASIC|sensor|actuator|motor|servo|stepper|encoder|gyroscope|accelerometer|magnetometer|IMU|GPS|LiDAR|camera|lidar|radar|ultrasonic|infrared|IR|temperature sensor|pressure sensor|force sensor|torque sensor|current sensor|voltage sensor|power supply|battery|charger|voltage regulator|DC-DC converter|AC-DC converter|transformer|relay|switch|button|potentiometer|joystick|display|LED|OLED|LCD|touchscreen|connector|pin|header|solder|soldering|breadboard|protoboard|oscilloscope|multimeter|function generator|logic analyzer|power supply|load|fixture|test equipment|calibration|tolerance|drift|noise|SNR|bandwidth|frequency|period|wavelength|amplitude|phase|modulation|demodulation|filter|amplifier|attenuator|impedance|resistance|capacitance|inductance|conductance|susceptance|admittance|reactance|resonance|filter|low-pass|high-pass|band-pass|band-stop|notch|all-pass|active|passive|analog|digital|ADC|DAC|sampling|quantization|aliasing|Nyquist|oversampling|undersampling|clock|timing|synchronization|trigger|edge|level|pulse|width|period|frequency|duty cycle|rise time|fall time|propagation delay|setup time|hold time|metastability|latch|flip-flop|register|counter|decoder|encoder|multiplexer|demultiplexer|adder|subtracter|multiplier|divider|comparator|voltage reference|current reference|precision|accuracy|resolution|linearity|monotonicity|INL|DNL|gain|offset|drift|temperature coefficient|package|footprint|thermal|heat sink|fan|cooling|ventilation|EMI|EMC|RFI|shielding|grounding|common mode|differential mode|CMRR|PSRR|gain bandwidth|slew rate|settling time|overshoot|undershoot|ringing|stability|compensation|feedback|loop gain|phase margin|gain margin|pole|zero|frequency response|Bode plot|Nyquist plot|root locus|step response|ramp response|impulse response|convolution|correlation|Fourier transform|Laplace transform|Z transform|discrete|continuous|linear|nonlinear|time invariant|time varying|causal|non-causal|stable|unstable|minimum phase|non-minimum phase|all-pass|minimum realization|canonical form|state space|transfer function|impulse response|frequency response|pole zero|stability|controllability|observability|reachability|detectability|controllable|observable|reachable|detectable|stabilizable|detectable)\b",
            r"\b(mechanical|mechanism|gear|pulley|belt|chain|bearing|shaft|coupling|clutch|brake|spring|damper|hydraulic|pneumatic|actuator|piston|cylinder|valve|compressor|motor|engine|combustion|thermodynamics|fluid dynamics|solid mechanics|materials|steel|aluminum|plastic|composite|strength|stiffness|ductility|hardness|fatigue|fracture|wear|corrosion|manufacturing|casting|forging|machining|milling|turning|grinding|welding|assembly|tolerance|fit|clearance|interference|GD&T|metrology|measurement|caliper|micrometer|gage|balance|scale|torque wrench|alignment|calibration|vibration|resonance|natural frequency|damping|stability|control|PID|feedback|feedforward|open loop|closed loop|controller|amplifier|driver|interface|connector|cable|harness|wire gauge|voltage|current|power|energy|efficiency|loss|heat|temperature|thermal management|cooling|heating|insulation|conduction|convection|radiation|radiative|convective|conductive|thermal resistance|thermal conductivity|junction|trace|copper pour|ground plane|power plane|signal integrity|impedance control|crosstalk|EMI|EMC|shielding|filtering|decoupling|bypass|bulk|ceramic|electrolytic|tantalum|film|resistor|carbon|metal film|thick film|thin film|potentiometer|trimmer|variable resistor|thermistor|varistor|photoresistor|LDR|photodiode|phototransistor|LED|laser diode|laser|optical|fiber|optic|lens|mirror|prism|filter|polarizer|waveguide|antenna|dipole|monopole|patch|yagi|parabolic|gain|directivity|beamwidth|polarization|impedance|SWR|VSWR|return loss|insertion loss|isolation|coupling|directivity|bandwidth|frequency|RF|microwave|millimeter wave|GHz|MHz|kHz|Hz|wavelength|propagation|attenuation|absorption|reflection|refraction|diffraction|scattering|fading|multipath|Doppler|Diversity|RAKE|MIMO|beamforming|phased array|smart antenna|adaptive antenna|SDR|software defined radio|RFIC|RFID|NFC|Bluetooth|WiFi|Zigbee|LoRa|cellular|LTE|5G|satellite|GPS|GNSS|INS|IMU|compass|magnetometer|accelerometer|gyroscope|barometer|altimeter|encoder|resolver|synchro|LVDT|RVT|potentiometric|optical encoder|magnetic encoder|Hall effect|MR|AMR|TMR|GMR|capacitive|inductive|eddy current|ultrasonic|radiation|x-ray|gamma ray|alpha|beta|neutron|dosimeter|spectrometer|mass spec|chromatograph|viscometer|densitometer|refractometer|spectrophotometer|colorimeter|polarimeter|ellipsometer|interferometer|profilometer|microscope|telescope|binoculars|camera|lens|aperture|focal length|f-number|depth of field|field of view|zoom|macro|telephoto|wide angle|normal|prime|zoom|fixed|varifocal|focus|autofocus|manual focus|shutter|speed|exposure|ISO|sensitivity|dynamic range|SNR|MTF|distortion|chromatic aberration|spherical aberration|coma|astigmatism|field curvature|vignetting|flare|ghosting|bokeh|perspective|tilt|shift|swing|perspective control|view camera|technical camera|medium format|large format|35mm|APS-C|full frame|crop factor|sensor|CCD|CMOS|Bayer|Foveon|monochrome|color|RGB|Bayer|quad Bayer|Remosaic|demosaicing|noise reduction|denoising|HDR|high dynamic range|tone mapping|local tone mapping|global tone mapping|color space|sRGB|Adobe RGB|ProPhoto RGB|Rec.2020|DCI-P3|gamut|white point|color temperature|D50|D65|illuminant|ICC|profile|color management|rendering intent|perceptual|relative colorimetric|absolute colorimetric|saturation|TRC|tone response curve|gamma|linear|log|HLG|PQ|BT.1886|BT.2100|HDR10|Dolby Vision|HDR10+|HLG|Hybrid Log-Gamma|Perceptual Quantizer|SMPTE ST 2084|ITU-R BT.2100|ITU-R BT.1886|CIE|XYZ|LAB|LUV|LCh|HSL|HSV|CMYK|RGB|RGBA|BGRA|ABGR|packed|planar|interleaved|chunky|planar|subsampled|4:4:4|4:2:2|4:2:0|4:1:1|3:1:1|JPEG|PNG|TIFF|BMP|GIF|WebP|HEIF|AVIF|JPEG XL|EXIF|metadata|tag|maker|model|serial number|firmware|version|date|time|timezone|GPS|coordinates|altitude|direction|orientation|flash|mode|power|fired|returned|FPD|function|red eye|white balance|mode|daylight|cloudy|shade|tungsten|fluorescent|flash|custom|Kelvin|tint|hue|saturation|contrast|sharpness|noise reduction|chroma|luma|luminance|chrominance|color difference|YCbCr|YCgCo|YPbPr|YUV|YIQ|HSV|HSL|CMYK|XYZ|LAB|LUV|xyY|RGB|RGBA|BGRA|ABGR|packed|planar|interleaved|chunky|planar|subsampled|4:4:4|4:2:2|4:2:0|4:1:1|3:1:1|JPEG|PNG|TIFF|BMP|GIF|WebP|HEIF|AVIF|JPEG XL|EXIF|metadata|tag|maker|model|serial number|firmware|version|date|time|timezone|GPS|coordinates|altitude|direction|orientation|flash|mode|power|fired|returned|FPD|function|red eye|white balance|mode|daylight|cloudy|shade|tungsten|fluorescent|flash|custom|Kelvin|tint|hue|saturation|contrast|sharpness|noise reduction|chroma|luma|luminance|chrominance|color difference|YCbCr|YCgCo|YPbPr|YUV|YIQ|HSV|HSL|CMYK|XYZ|LAB|LUV|xyY)\b"
        ]
    
    def extract_content_elements(self, content: str) -> PersonalizationFilter:
        """
        Analyze content and identify software/hardware-specific elements
        
        Args:
            content: The content to analyze
            
        Returns:
            PersonalizationFilter with categorized elements
        """
        lines = content.split('\n')
        result = PersonalizationFilter()
        
        for i, line in enumerate(lines):
            # Check for software-specific patterns
            if any(re.search(pattern, line, re.IGNORECASE) for pattern in self.software_patterns):
                result.software_elements.append(f"{i}:{line.strip()}")
            
            # Check for hardware-specific patterns
            elif any(re.search(pattern, line, re.re.IGNORECASE) for pattern in self.hardware_patterns):
                result.hardware_elements.append(f"{i}:{line.strip()}")
            
            # Otherwise, it's neutral content
            else:
                result.neutral_elements.append(f"{i}:{line.strip()}")
        
        return result
    
    def personalize_content(self, content: str, user_background: BackgroundType) -> str:
        """
        Filter content based on user background
        
        Args:
            content: Original content
            user_background: User's background type
            
        Returns:
            Personalized content based on user background
        """
        lines = content.split('\n')
        result_lines = []
        
        for i, line in enumerate(lines):
            is_software_related = any(re.search(pattern, line, re.IGNORECASE) for pattern in self.software_patterns)
            is_hardware_related = any(re.search(pattern, line, re.IGNORECASE) for pattern in self.hardware_patterns)
            
            # Show line based on user background
            if user_background == BackgroundType.BOTH:
                # Show all content
                result_lines.append(line)
            elif user_background == BackgroundType.SOFTWARE:
                # Show software-related and neutral content
                if not is_hardware_related:
                    result_lines.append(line)
            elif user_background == BackgroundType.HARDWARE:
                # Show hardware-related and neutral content
                if not is_software_related:
                    result_lines.append(line)
            else:
                # Default: show all content
                result_lines.append(line)
        
        return '\n'.join(result_lines)
    
    def get_user_background(self, user_id: str) -> Optional[BackgroundType]:
        """
        Retrieve user background from the database
        
        Args:
            user_id: The ID of the user
            
        Returns:
            BackgroundType for the user, or None if not found
        """
        # This would normally query the database
        # For now, returning None as a placeholder
        # In a real implementation, this would connect to the Neon database
        # and retrieve the user's background from the users table
        return None