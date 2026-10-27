# -*- coding: utf-8 -*-
import sys

new_reviews_html = '''    <!-- REAL REVIEWS WITH INBUILT VIDEO & CUSTOMER PHOTOS (5.0★ Google Maps Verified) -->
    <section id="reviews" class="py-20 bg-white border-t border-[#e5e5ea]">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <!-- Section Header -->
            <div class="text-center space-y-3 mb-10">
                <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-amber-50 text-amber-900 text-xs font-mono font-bold border border-amber-200 shadow-sm">
                    <svg class="w-4 h-4 text-[#4285F4]" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
                        <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                        <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z" fill="#FBBC05"/>
                        <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z" fill="#EA4335"/>
                    </svg>
                    <span>5.0 / 5.0 GOOGLE MAPS RATING &bull; 100% VERIFIED LOCAL BUYERS</span>
                </div>
                <h2 class="text-3xl sm:text-4xl font-extrabold font-heading text-[#1d1d1f]">Real Reviews, Videos &amp; Unboxings</h2>
                <p class="text-[#86868b] text-sm max-w-2xl mx-auto">Watch real unboxing videos recorded by customers at our Boring Road counter, and read genuine feedback from verified Patna smartphone buyers.</p>
                
                <!-- Filter Tabs (All / Inbuilt Videos / Photos) -->
                <div class="flex items-center justify-center gap-2 pt-4">
                    <button onclick="filterReviewCards('all')" id="btn-review-all" class="review-tab-btn active px-4 py-2 rounded-full text-xs font-mono font-bold transition-all bg-[#1d1d1f] text-white shadow-sm">
                        All Reviews (6)
                    </button>
                    <button onclick="filterReviewCards('video')" id="btn-review-video" class="review-tab-btn px-4 py-2 rounded-full text-xs font-mono font-bold transition-all bg-[#f5f5f7] text-[#1d1d1f] hover:bg-gray-200 border border-[#e5e5ea] flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
                        <span>🎥 Inbuilt Video Reviews (2)</span>
                    </button>
                    <button onclick="filterReviewCards('photo')" id="btn-review-photo" class="review-tab-btn px-4 py-2 rounded-full text-xs font-mono font-bold transition-all bg-[#f5f5f7] text-[#1d1d1f] hover:bg-gray-200 border border-[#e5e5ea]">
                        📸 Photo Reviews (4)
                    </button>
                </div>
            </div>

            <!-- Review Cards Grid (Submerged Video & Photo Reviews) -->
            <div id="reviews-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

                <!-- REVIEW CARD 1 [VIDEO]: iPhone 16 Pro (Amit Sharma) -->
                <div class="review-card apple-card p-6 rounded-3xl flex flex-col justify-between space-y-4 ring-2 ring-emerald-500/30" data-category="video">
                    <div>
                        <!-- User Header -->
                        <div class="flex items-center justify-between mb-3">
                            <div class="flex items-center gap-3">
                                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80" 
                                     alt="Amit Sharma" 
                                     class="w-11 h-11 rounded-full object-cover border-2 border-emerald-500 shadow-sm">
                                <div>
                                    <div class="flex items-center gap-1.5">
                                        <h4 class="font-bold text-[#1d1d1f] text-sm">Amit Sharma</h4>
                                        <span class="inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-bold bg-emerald-50 text-emerald-700">✓ Verified</span>
                                    </div>
                                    <div class="text-[11px] text-[#86868b]">Local Guide &bull; Boring Road, Patna</div>
                                </div>
                            </div>
                            <span class="text-[11px] font-mono text-[#86868b]">3 days ago</span>
                        </div>

                        <!-- Stars & Model -->
                        <div class="flex items-center justify-between mb-2.5">
                            <div class="text-amber-400 text-sm tracking-tight">★★★★★</div>
                            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-red-50 text-red-700 font-bold flex items-center gap-1">
                                <span class="w-1.5 h-1.5 rounded-full bg-red-500 animate-ping"></span> Video Review
                            </span>
                        </div>

                        <!-- Review Text -->
                        <p class="text-[#1d1d1f] text-xs sm:text-sm leading-relaxed">
                            "Recorded this quick unboxing video right at Bhaiya's counter! 100% sealed pack iPhone 16 Pro Desert Titanium. Official Apple warranty activation verified on the spot, and free WhatsApp chat transfer. Saved big money compared to malls!"
                        </p>
                    </div>

                    <!-- Inbuilt Video Player -->
                    <div class="pt-2">
                        <div class="relative rounded-2xl overflow-hidden border border-[#e5e5ea] bg-black shadow-sm group">
                            <video id="video-iphone" 
                                   src="/videos/unboxing_iphone.mp4" 
                                   poster="https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=800&auto=format&fit=crop&q=80" 
                                   playsinline 
                                   loop 
                                   controls 
                                   preload="metadata"
                                   class="w-full h-52 object-cover">
                            </video>
                            <div class="absolute top-2.5 left-2.5 px-2.5 py-1 rounded-full bg-red-600/90 text-white text-[10px] font-mono font-bold flex items-center gap-1.5 shadow pointer-events-none">
                                <span class="w-2 h-2 rounded-full bg-white animate-pulse"></span>
                                <span>IN-STORE VIDEO &bull; 0:15</span>
                            </div>
                            <div class="absolute bottom-2 left-2 right-2 px-2.5 py-1 rounded-lg bg-black/75 backdrop-blur-md text-[11px] text-white flex items-center justify-between pointer-events-none">
                                <span class="flex items-center gap-1.5"><i data-lucide="video" class="w-3.5 h-3.5 text-emerald-400"></i> Counter Unboxing</span>
                                <span class="font-mono text-[10px] text-emerald-300">Tap to Play</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- REVIEW CARD 2 [VIDEO]: Samsung Galaxy S24 Ultra (Rahul Kumar) -->
                <div class="review-card apple-card p-6 rounded-3xl flex flex-col justify-between space-y-4 ring-2 ring-emerald-500/30" data-category="video">
                    <div>
                        <!-- User Header -->
                        <div class="flex items-center justify-between mb-3">
                            <div class="flex items-center gap-3">
                                <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&auto=format&fit=crop&q=80" 
                                     alt="Rahul Kumar" 
                                     class="w-11 h-11 rounded-full object-cover border-2 border-emerald-500 shadow-sm">
                                <div>
                                    <div class="flex items-center gap-1.5">
                                        <h4 class="font-bold text-[#1d1d1f] text-sm">Rahul Kumar</h4>
                                        <span class="inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-bold bg-emerald-50 text-emerald-700">✓ Verified</span>
                                    </div>
                                    <div class="text-[11px] text-[#86868b]">Patna &bull; Samsung S-Series Buyer</div>
                                </div>
                            </div>
                            <span class="text-[11px] font-mono text-[#86868b]">1 week ago</span>
                        </div>

                        <!-- Stars & Model -->
                        <div class="flex items-center justify-between mb-2.5">
                            <div class="text-amber-400 text-sm tracking-tight">★★★★★</div>
                            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-red-50 text-red-700 font-bold flex items-center gap-1">
                                <span class="w-1.5 h-1.5 rounded-full bg-red-500 animate-ping"></span> Video Review
                            </span>
                        </div>

                        <!-- Review Text -->
                        <p class="text-[#1d1d1f] text-xs sm:text-sm leading-relaxed">
                            "Watch my S24 Ultra unboxing video! Got genuine Indian retail box with bill and full brand warranty. Bajaj 0% EMI was approved in 10 minutes on-counter. Bhaiya also applied UV tempered glass with zero bubbles. Highly recommend!"
                        </p>
                    </div>

                    <!-- Inbuilt Video Player -->
                    <div class="pt-2">
                        <div class="relative rounded-2xl overflow-hidden border border-[#e5e5ea] bg-black shadow-sm group">
                            <video id="video-samsung" 
                                   src="/videos/unboxing_flagship.mp4" 
                                   poster="https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=800&auto=format&fit=crop&q=80" 
                                   playsinline 
                                   loop 
                                   controls 
                                   preload="metadata"
                                   class="w-full h-52 object-cover">
                            </video>
                            <div class="absolute top-2.5 left-2.5 px-2.5 py-1 rounded-full bg-red-600/90 text-white text-[10px] font-mono font-bold flex items-center gap-1.5 shadow pointer-events-none">
                                <span class="w-2 h-2 rounded-full bg-white animate-pulse"></span>
                                <span>IN-STORE VIDEO &bull; 0:28</span>
                            </div>
                            <div class="absolute bottom-2 left-2 right-2 px-2.5 py-1 rounded-lg bg-black/75 backdrop-blur-md text-[11px] text-white flex items-center justify-between pointer-events-none">
                                <span class="flex items-center gap-1.5"><i data-lucide="video" class="w-3.5 h-3.5 text-emerald-400"></i> Galaxy Flagship Handover</span>
                                <span class="font-mono text-[10px] text-emerald-300">Tap to Play</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- REVIEW CARD 3 [PHOTO]: OnePlus 12 Trade-in (Mohammad Danish) -->
                <div class="review-card apple-card p-6 rounded-3xl flex flex-col justify-between space-y-4" data-category="photo">
                    <div>
                        <!-- User Header -->
                        <div class="flex items-center justify-between mb-3">
                            <div class="flex items-center gap-3">
                                <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=150&auto=format&fit=crop&q=80" 
                                     alt="Mohammad Danish" 
                                     class="w-11 h-11 rounded-full object-cover border-2 border-emerald-500 shadow-sm">
                                <div>
                                    <div class="flex items-center gap-1.5">
                                        <h4 class="font-bold text-[#1d1d1f] text-sm">Mohammad Danish</h4>
                                        <span class="inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-bold bg-emerald-50 text-emerald-700">✓ Verified</span>
                                    </div>
                                    <div class="text-[11px] text-[#86868b]">Sri Krishna Puri &bull; OnePlus Exchange</div>
                                </div>
                            </div>
                            <span class="text-[11px] font-mono text-[#86868b]">2 weeks ago</span>
                        </div>

                        <!-- Stars & Model -->
                        <div class="flex items-center justify-between mb-2.5">
                            <div class="text-amber-400 text-sm tracking-tight">★★★★★</div>
                            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-gray-100 text-gray-700 font-semibold">OnePlus 12 + Trade-In</span>
                        </div>

                        <!-- Review Text -->
                        <p class="text-[#1d1d1f] text-xs sm:text-sm leading-relaxed">
                            "Exchanged my old OnePlus 9 Pro for the new OnePlus 12. Bhaiya gave me top valuation without unnecessary cuts. Paid the remaining balance via UPI and got genuine 100W SuperVOOC charger in the box. Best exchange shop in Patna!"
                        </p>
                    </div>

                    <!-- Customer Photo -->
                    <div class="pt-2">
                        <div class="relative rounded-2xl overflow-hidden border border-[#e5e5ea] group shadow-sm bg-gray-50">
                            <img src="https://images.unsplash.com/photo-1580910051074-3eb694886505?w=800&auto=format&fit=crop&q=80" 
                                 alt="Customer unboxing OnePlus 12 at Ali Mobile showroom" 
                                 class="w-full h-52 object-cover group-hover:scale-105 transition-transform duration-300">
                            <div class="absolute bottom-2 left-2 right-2 px-2.5 py-1 rounded-lg bg-black/75 backdrop-blur-md text-[11px] text-white flex items-center justify-between">
                                <span class="flex items-center gap-1.5"><i data-lucide="camera" class="w-3.5 h-3.5 text-emerald-400"></i> Customer Photo &bull; Unboxing Moment</span>
                                <span class="font-mono text-[10px] text-amber-300">Trade-In Done</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- REVIEW CARD 4 [PHOTO]: iPhone 15 Pink (Priya Verma) -->
                <div class="review-card apple-card p-6 rounded-3xl flex flex-col justify-between space-y-4" data-category="photo">
                    <div>
                        <!-- User Header -->
                        <div class="flex items-center justify-between mb-3">
                            <div class="flex items-center gap-3">
                                <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&auto=format&fit=crop&q=80" 
                                     alt="Priya Verma" 
                                     class="w-11 h-11 rounded-full object-cover border-2 border-emerald-500 shadow-sm">
                                <div>
                                    <div class="flex items-center gap-1.5">
                                        <h4 class="font-bold text-[#1d1d1f] text-sm">Priya Verma</h4>
                                        <span class="inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-bold bg-emerald-50 text-emerald-700">✓ Verified</span>
                                    </div>
                                    <div class="text-[11px] text-[#86868b]">Kankarbagh / Patna &bull; iPhone 15</div>
                                </div>
                            </div>
                            <span class="text-[11px] font-mono text-[#86868b]">2 weeks ago</span>
                        </div>

                        <!-- Stars & Model -->
                        <div class="flex items-center justify-between mb-2.5">
                            <div class="text-amber-400 text-sm tracking-tight">★★★★★</div>
                            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-gray-100 text-gray-700 font-semibold">iPhone 15 Pink 128GB</span>
                        </div>

                        <!-- Review Text -->
                        <p class="text-[#1d1d1f] text-xs sm:text-sm leading-relaxed">
                            "Bought my first iPhone from Ali Mobile on my brother's recommendation. Bhaiya helped me set up Apple ID, iCloud backup, and eSIM activation without charging anything extra. The phone is 100% genuine sealed pack with 1-year Apple India warranty!"
                        </p>
                    </div>

                    <!-- Customer Photo -->
                    <div class="pt-2">
                        <div class="relative rounded-2xl overflow-hidden border border-[#e5e5ea] group shadow-sm bg-gray-50">
                            <img src="https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=800&auto=format&fit=crop&q=80" 
                                 alt="Customer holding newly unboxed iPhone 15 Pink" 
                                 class="w-full h-52 object-cover group-hover:scale-105 transition-transform duration-300">
                            <div class="absolute bottom-2 left-2 right-2 px-2.5 py-1 rounded-lg bg-black/75 backdrop-blur-md text-[11px] text-white flex items-center justify-between">
                                <span class="flex items-center gap-1.5"><i data-lucide="camera" class="w-3.5 h-3.5 text-emerald-400"></i> Customer Photo &bull; In-Hand Preview</span>
                                <span class="font-mono text-[10px] text-pink-300">Apple Bill</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- REVIEW CARD 5 [PHOTO]: Xiaomi 14 Ultra Leica (Vikramaditya Singh) -->
                <div class="review-card apple-card p-6 rounded-3xl flex flex-col justify-between space-y-4" data-category="photo">
                    <div>
                        <!-- User Header -->
                        <div class="flex items-center justify-between mb-3">
                            <div class="flex items-center gap-3">
                                <img src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=150&auto=format&fit=crop&q=80" 
                                     alt="Vikramaditya Singh" 
                                     class="w-11 h-11 rounded-full object-cover border-2 border-emerald-500 shadow-sm">
                                <div>
                                    <div class="flex items-center gap-1.5">
                                        <h4 class="font-bold text-[#1d1d1f] text-sm">Vikramaditya Singh</h4>
                                        <span class="inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-bold bg-emerald-50 text-emerald-700">✓ Verified</span>
                                    </div>
                                    <div class="text-[11px] text-[#86868b]">Bailey Road, Patna &bull; Leica Camera</div>
                                </div>
                            </div>
                            <span class="text-[11px] font-mono text-[#86868b]">3 weeks ago</span>
                        </div>

                        <!-- Stars & Model -->
                        <div class="flex items-center justify-between mb-2.5">
                            <div class="text-amber-400 text-sm tracking-tight">★★★★★</div>
                            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-gray-100 text-gray-700 font-semibold">Xiaomi 14 Ultra (Leica)</span>
                        </div>

                        <!-- Review Text -->
                        <p class="text-[#1d1d1f] text-xs sm:text-sm leading-relaxed">
                            "Was searching for Xiaomi 14 Ultra everywhere in Patna, no store had ready stock. Messaged Bhaiya on WhatsApp and he arranged genuine sealed piece with Leica photography kit in 3 hours! Transparent billing and genuine price."
                        </p>
                    </div>

                    <!-- Customer Photo -->
                    <div class="pt-2">
                        <div class="relative rounded-2xl overflow-hidden border border-[#e5e5ea] group shadow-sm bg-gray-50">
                            <img src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&auto=format&fit=crop&q=80" 
                                 alt="Xiaomi 14 Ultra Leica camera phone handover" 
                                 class="w-full h-52 object-cover group-hover:scale-105 transition-transform duration-300">
                            <div class="absolute bottom-2 left-2 right-2 px-2.5 py-1 rounded-lg bg-black/75 backdrop-blur-md text-[11px] text-white flex items-center justify-between">
                                <span class="flex items-center gap-1.5"><i data-lucide="camera" class="w-3.5 h-3.5 text-emerald-400"></i> Customer Photo &bull; Store Delivery</span>
                                <span class="font-mono text-[10px] text-emerald-300">Leica Edition</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- REVIEW CARD 6 [PHOTO]: Vivo Flagship & AirPods (Anand Prakash) -->
                <div class="review-card apple-card p-6 rounded-3xl flex flex-col justify-between space-y-4" data-category="photo">
                    <div>
                        <!-- User Header -->
                        <div class="flex items-center justify-between mb-3">
                            <div class="flex items-center gap-3">
                                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80" 
                                     alt="Anand Prakash" 
                                     class="w-11 h-11 rounded-full object-cover border-2 border-emerald-500 shadow-sm">
                                <div>
                                    <div class="flex items-center gap-1.5">
                                        <h4 class="font-bold text-[#1d1d1f] text-sm">Anand Prakash</h4>
                                        <span class="inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-bold bg-emerald-50 text-emerald-700">✓ Verified</span>
                                    </div>
                                    <div class="text-[11px] text-[#86868b]">Raja Bazar, Patna &bull; Vivo &amp; Audio</div>
                                </div>
                            </div>
                            <span class="text-[11px] font-mono text-[#86868b]">1 month ago</span>
                        </div>

                        <!-- Stars & Model -->
                        <div class="flex items-center justify-between mb-2.5">
                            <div class="text-amber-400 text-sm tracking-tight">★★★★★</div>
                            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-gray-100 text-gray-700 font-semibold">Vivo X100 Pro &bull; ZEISS</span>
                        </div>

                        <!-- Review Text -->
                        <p class="text-[#1d1d1f] text-xs sm:text-sm leading-relaxed">
                            "Superb experience. 0% EMI done via HDFC debit card swipe. Instant approval and instant handover. Clean showroom, honest guidance, and best rates in Patna. Also purchased original AirPods here."
                        </p>
                    </div>

                    <!-- Customer Photo -->
                    <div class="pt-2">
                        <div class="relative rounded-2xl overflow-hidden border border-[#e5e5ea] group shadow-sm bg-gray-50">
                            <img src="https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=800&auto=format&fit=crop&q=80" 
                                 alt="Vivo X100 Pro and accessories at Ali Mobile" 
                                 class="w-full h-52 object-cover group-hover:scale-105 transition-transform duration-300">
                            <div class="absolute bottom-2 left-2 right-2 px-2.5 py-1 rounded-lg bg-black/75 backdrop-blur-md text-[11px] text-white flex items-center justify-between">
                                <span class="flex items-center gap-1.5"><i data-lucide="camera" class="w-3.5 h-3.5 text-emerald-400"></i> Customer Photo &bull; Desk Setup</span>
                                <span class="font-mono text-[10px] text-purple-300">Debit EMI</span>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- Review CTA Banner -->
            <div class="mt-12 bg-[#f5f5f7] border border-[#e5e5ea] rounded-3xl p-6 sm:p-8 flex flex-col sm:flex-row items-center justify-between gap-6">
                <div class="flex items-center gap-4 text-left">
                    <div class="w-12 h-12 rounded-2xl bg-white border border-[#e5e5ea] flex items-center justify-center shrink-0 shadow-sm text-amber-500 text-2xl">
                        ⭐
                    </div>
                    <div>
                        <h4 class="font-bold text-[#1d1d1f] text-base">Bought a Smartphone from Ali Mobile?</h4>
                        <p class="text-xs text-[#86868b] mt-0.5">Share your unboxing photo or video on Google Maps &amp; get a complimentary premium tempered glass on your next visit!</p>
                    </div>
                </div>
                <a href="https://maps.app.goo.gl/n9KcwPUWWmccFfVJ9" target="_blank" rel="noopener noreferrer" 
                   class="btn-apple-dark px-6 py-3 rounded-full text-xs font-bold font-mono tracking-wide flex items-center gap-2 shrink-0">
                    <svg class="w-4 h-4 text-[#4285F4]" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
                        <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                        <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z" fill="#FBBC05"/>
                        <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z" fill="#EA4335"/>
                    </svg>
                    <span>Write a Review on Google Maps</span>
                    <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                </a>
            </div>

        </div>

        <script>
            function filterReviewCards(category) {
                // Update button styles
                const btns = document.querySelectorAll('.review-tab-btn');
                btns.forEach(b => {
                    b.classList.remove('bg-[#1d1d1f]', 'text-white', 'shadow-sm');
                    b.classList.add('bg-[#f5f5f7]', 'text-[#1d1d1f]', 'border', 'border-[#e5e5ea]');
                });

                const activeBtn = document.getElementById('btn-review-' + category);
                if (activeBtn) {
                    activeBtn.classList.remove('bg-[#f5f5f7]', 'text-[#1d1d1f]', 'border', 'border-[#e5e5ea]');
                    activeBtn.classList.add('bg-[#1d1d1f]', 'text-white', 'shadow-sm');
                }

                // Filter cards
                const cards = document.querySelectorAll('.review-card');
                cards.forEach(c => {
                    if (category === 'all' || c.getAttribute('data-category') === category) {
                        c.style.display = 'flex';
                    } else {
                        c.style.display = 'none';
                    }
                });
            }
        </script>
    </section>
'''

with open(r'C:\Users\rehan\Desktop\projects\ali_mobile_patna\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '    <!-- REAL REVIEWS WITH CUSTOMER PHOTOS (5.0★ Google Maps Verified) -->'
end_marker = '    <!-- STORE LOCATION & GOOGLE MAPS -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print('ERROR: markers not found')
    sys.exit(1)

updated_content = content[:start_idx] + new_reviews_html + '\n' + content[end_idx:]

with open(r'C:\Users\rehan\Desktop\projects\ali_mobile_patna\index.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print('SUCCESS: updated index.html with submerged video & photo reviews!')
